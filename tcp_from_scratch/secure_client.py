"""
A secure TCP client implementation at the core level:
- Diffie-Hellman for key exchange
- AES for encryption
- HMAC for message authentication

Author: Usama Munir
Date: Nov 26th, 2024
"""

import socket
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hmac
import hashlib

# Diffie-Hellman Parameters (must match the server)
PRIME = 23  # Public prime number (shared)
BASE = 5    # Public base (shared)

# Shared HMAC Key (used to verify message integrity)
HMAC_KEY = b'shared_hmac_key'


def start_secure_client(host="127.0.0.1", port=5555):
    """
    Starts a secure TCP client that uses:
    - Diffie-Hellman for key exchange
    - AES for encryption
    - HMAC for integrity verification

    Parameters:
    - host (str): Server IP address.
    - port (int): Server port.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"[INFO] Connected to secure server at {host}:{port}")

    # Step 1: Diffie-Hellman Key Exchange
    client_private = random.randint(1, PRIME - 1)  # Private key
    client_public = pow(BASE, client_private, PRIME)  # Public key
    print(f"[DEBUG] Client public key: {client_public}")

    server_public = int(client_socket.recv(1024).decode())  # Receive public key from server
    client_socket.send(str(client_public).encode())  # Send public key to server
    shared_secret = pow(server_public, client_private, PRIME)  # Compute shared secret
    print(f"[DEBUG] Shared secret computed: {shared_secret}")

    # Step 2: Derive AES key from shared secret
    aes_key = str(shared_secret).zfill(16)[:16].encode()  # Ensure key length is 16 bytes

    # Step 3: Send Initialization Vector (IV)
    cipher = AES.new(aes_key, AES.MODE_CBC)  # Create AES cipher
    iv = cipher.iv
    client_socket.send(iv)
    print(f"[DEBUG] Sent IV: {iv.hex()}")

    # Step 4: Encrypt and Send Message
    message = "Hello, secure server!"  # Message to encrypt
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))  # Encrypt and pad the message
    client_socket.send(ciphertext)
    print(f"[INFO] Encrypted message sent.")

    # Step 5: Generate and Send HMAC
    message_hmac = hmac.new(HMAC_KEY, message.encode(), hashlib.sha256).digest()
    client_socket.send(message_hmac)
    print(f"[INFO] HMAC sent.")

    client_socket.close()


if __name__ == "__main__":
    start_secure_client()
