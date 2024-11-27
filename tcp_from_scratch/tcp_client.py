"""
tcp_client.py

A simplified implementation of a TCP client using sockets. 
This script demonstrates the core principles of TCP:
- Three-Way Handshake (SYN, SYN-ACK, ACK)
- Data Transmission
- Connection Termination (FIN, ACK)

Author: [Your Name]
Date: [Today's Date]
"""

import socket

# Constants for the custom TCP protocol
SYN = "SYN"
ACK = "ACK"
SYN_ACK = "SYN-ACK"
FIN = "FIN"

def tcp_client(server_host="127.0.0.1", server_port=5555):
    """
    Connect to the TCP server and perform:
    - Handshake
    - Data exchange
    - Connection termination
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    # Three-Way Handshake
    print("[DEBUG] Sending SYN")
    client_socket.send(SYN.encode())  # Send SYN
    msg = client_socket.recv(1024).decode()
    if msg == SYN_ACK:
        print("[DEBUG] Received SYN-ACK")
        client_socket.send(ACK.encode())  # Send ACK
        msg = client_socket.recv(1024).decode()
        print("[DEBUG] Server response:", msg)

    # Data Transmission
    for i in range(5):
        message = f"Message {i+1}"
        print(f"[DEBUG] Sending: {message}")
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print("[DEBUG] Server echoed:", response)

    # Connection Termination
    print("[DEBUG] Sending FIN")
    client_socket.send(FIN.encode())
    ack = client_socket.recv(1024).decode()
    if ack == ACK:
        print("[DEBUG] Received ACK - Connection Closed")
    client_socket.close()


if __name__ == "__main__":
    tcp_client()
