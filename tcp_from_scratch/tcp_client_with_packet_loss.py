"""
A TCP client with packet loss simulation and retry mechanism.
"""

import socket
import random
import time

# Constants
SYN = "SYN"
ACK = "ACK"
SYN_ACK = "SYN-ACK"
FIN = "FIN"

PACKET_LOSS_RATE = 0.2  # 20% packet loss


def send_with_packet_loss(sock, data):
    """
    Simulates packet loss by randomly dropping packets.
    """
    if random.random() > PACKET_LOSS_RATE:
        sock.sendall(data.encode())
        print(f"[SENT] {data}")
    else:
        print(f"[DROPPED] {data}")


def tcp_client_with_packet_loss(server_host="127.0.0.1", server_port=5555):
    """
    A TCP client that handles packet loss during communication.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    # Step 1: Three-Way Handshake
    print("[DEBUG] Sending SYN")
    send_with_packet_loss(client_socket, SYN)  # Send SYN

    try:
        msg = client_socket.recv(1024).decode()
        if msg == SYN_ACK:
            print("[DEBUG] Received SYN-ACK")
            send_with_packet_loss(client_socket, ACK)  # Send ACK
            msg = client_socket.recv(1024).decode()
            print("[DEBUG] Server response:", msg)
    except socket.timeout:
        print("[ERROR] Timeout during handshake")

    # Step 2: Data Transmission
    for i in range(5):
        message = f"Message {i+1}"
        while True:  # Retry until the server acknowledges the message
            send_with_packet_loss(client_socket, message)
            try:
                response = client_socket.recv(1024).decode()
                if response.startswith("Echo:"):
                    print(f"[DEBUG] Server echoed: {response}")
                    break
            except socket.timeout:
                print("[RETRY] Retrying message:", message)

    # Step 3: Connection Termination
    print("[DEBUG] Sending FIN")
    send_with_packet_loss(client_socket, FIN)
    try:
        ack = client_socket.recv(1024).decode()
        if ack == ACK:
            print("[DEBUG] Received ACK - Connection Closed")
    except socket.timeout:
        print("[ERROR] Timeout during connection termination")

    client_socket.close()


if __name__ == "__main__":
    tcp_client_with_packet_loss()
