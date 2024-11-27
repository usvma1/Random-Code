"""
A secure TCP server implementation at the core level:
- Diffie-Hellman for key exchange
- AES for encryption
- HMAC for message authentication

Author: Usama Munir
Date: Nov 26th, 2024
"""

import socket
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hmac
import hashlib

# Diffie-Hellman Parameters (simplified for educational purposes)
PRIME = 23  # Public prime number (shared by client and server)
BASE = 5    # Public base (shared by client and server)

# Shared HMAC Key (used to verify message integrity)
HMAC_KEY = b'shared_hmac_key'


def start_secure_server(host="127.0.0.1", port=5555):
    """
    Starts a secure TCP server that uses:
    - Diffie-Hellman for key exchange
    - AES for encryption
    - HMAC for integrity verification

    Parameters:
    - host (str): IP address to bind the server.
    - port (int): Port to bind the server.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[INFO] Secure server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"[INFO] Connection established with {addr}")

    # Step 1: Diffie-Hellman Key Exchange
    server_private = random.randint(1, PRIME - 1)  # Private key
    server_public = pow(BASE, server_private, PRIME)  # Public key
    print(f"[DEBUG] Server public key: {server_public}")

    client_socket.send(str(server_public).encode())  # Send public key to client
    client_public = int(client_socket.recv(1024).decode())  # Receive public key from client
    shared_secret = pow(client_public, server_private, PRIME)  # Compute shared secret
    print(f"[DEBUG] Shared secret computed: {shared_secret}")

    # Step 2: Derive AES key from shared secret
    aes_key = str(shared_secret).zfill(16)[:16].encode()  # Ensure key length is 16 bytes

    # Step 3: Receive Initialization Vector (IV)
    iv = client_socket.recv(1024)
    print(f"[DEBUG] Received IV: {iv.hex()}")

    # Step 4: Receive Encrypted Message
    ciphertext = client_socket.recv(1024)
    print(f"[DEBUG] Received ciphertext: {ciphertext.hex()}")

    cipher = AES.new(aes_key, AES.MODE_CBC, iv)  # Create AES cipher
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Decrypt and unpad the message
    print(f"[INFO] Decrypted plaintext: {plaintext.decode()}")

    # Step 5: Validate HMAC
    received_hmac = client_socket.recv(1024)
    print(f"[DEBUG] Received HMAC: {received_hmac.hex()}")

    computed_hmac = hmac.new(HMAC_KEY, plaintext, hashlib.sha256).digest()
    if hmac.compare_digest(received_hmac, computed_hmac):
        print("[INFO] Message authentication succeeded.")
    else:
        print("[ERROR] Message authentication failed.")

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_secure_server()
