# TCP from Scratch

This project demonstrates a simplified implementation of TCP using Python. It mimics core TCP principles, including:

- **Three-Way Handshake**: Connection establishment using SYN, SYN-ACK, and ACK messages.
- **Data Transmission**: Echoing messages back to the client.
- **Connection Termination**: Gracefully closing the connection using FIN and ACK messages.

---

## **Features**

1. **Connection Establishment**:
   - Implements the TCP three-way handshake (SYN, SYN-ACK, ACK).
2. **Data Transmission**:
   - Allows clients to send messages to the server, which are echoed back.
3. **Connection Termination**:
   - Simulates the TCP connection closure process (FIN, ACK).
4. **Logging**:
   - Tracks events like connection establishment, data transfer, and termination.
5. **Packet Loss Simulation**:
   - Introduces packet loss during transmission for educational purposes.
   - Includes a retry mechanism to ensure reliable communication.
6. **Secure Communication**:
   - Implements end-to-end secure communication using:
     - **Diffie-Hellman**: For secure key exchange.
     - **AES**: For encrypting transmitted data.
     - **HMAC**: For ensuring data integrity and authenticity.
7. **Retry Mechanism**:
   - Retries dropped packets until an acknowledgment is received.

---

## **Files**

### Core Implementation
- **`tcp_server.py`**:
  - The server-side implementation of the TCP functionality.
- **`tcp_client.py`**:
  - The client-side implementation for interacting with the server.

### Enhanced Features
- **`tcp_logging.py`**:
  - A utility for logging events to a file or console.
- **`tcp_client_with_packet_loss.py`**:
  - Client implementation with packet loss simulation and retry mechanism.
- **`tcp_server_with_packet_loss.py`**:
  - Server implementation for handling packet loss during communication.

### Secure Communication
- **`secure_server.py`**:
  - A server implementation with secure communication using Diffie-Hellman, AES, and HMAC.
- **`secure_client.py`**:
  - A client implementation complementing `secure_server.py` for secure communication.

### Testing
- **`test_tcp.py`**:
  - Contains tests for client-server communication and feature validation.

---

## **How to Run**

### **1. Run the Server**
Start the server in one terminal:

```bash
python tcp_server.py
```

To use the packet loss feature, start the server with packet loss handling:

```bash
python tcp_server_with_packet_loss.py
```

For secure communication, start the secure server:

```bash
python secure_server.py
```

### **2. Run the Client**
Start the client in another terminal:

```bash
python tcp_client.py
```

To simulate packet loss, use:

```bash
python tcp_client_with_packet_loss.py
```

For secure communication, use the secure client:

```bash
python secure_client.py
```
