"""
tcp_server.py

A simplified implementation of a TCP server using sockets. 
This script demonstrates the core principles of TCP:
- Three-Way Handshake (SYN, SYN-ACK, ACK)
- Data Transmission
- Connection Termination (FIN, ACK)

Author: Usama Munir
Date: Nov 26th, 2024
"""

import socket
import threading

# Constants for the custom TCP protocol
SYN = "SYN"
ACK = "ACK"
SYN_ACK = "SYN-ACK"
FIN = "FIN"

def handle_client(client_socket, address):
    """
    Handle client communication:
    - Perform the handshake
    - Echo received data
    - Close the connection on FIN signal
    """
    print(f"[INFO] Connection initiated by {address}")

    # Three-Way Handshake
    msg = client_socket.recv(1024).decode()
    if msg == SYN:
        print("[DEBUG] Received SYN")
        client_socket.send(SYN_ACK.encode())  # Send SYN-ACK

        msg = client_socket.recv(1024).decode()
        if msg == ACK:
            print("[DEBUG] Received ACK - Connection Established")
            client_socket.send("Connection Established".encode())
        else:
            print("[ERROR] Expected ACK, received:", msg)
            client_socket.close()
            return

    # Data Transmission
    while True:
        data = client_socket.recv(1024).decode()
        if data == FIN:
            print("[DEBUG] Received FIN - Closing Connection")
            client_socket.send(ACK.encode())
            break
        print(f"[DATA] Received: {data}")
        client_socket.send(f"Echo: {data}".encode())

    # Connection Termination
    client_socket.close()
    print(f"[INFO] Connection closed with {address}")


def start_server(host="127.0.0.1", port=5555):
    """
    Start the TCP server and listen for connections.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[INFO] Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()


if __name__ == "__main__":
    start_server()
