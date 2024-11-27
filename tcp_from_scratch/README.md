# TCP from Scratch

This project demonstrates a simplified implementation of TCP using Python. It mimics core TCP principles, including:
- Three-Way Handshake (SYN, SYN-ACK, ACK)
- Data Transmission
- Connection Termination (FIN, ACK)

## Files
- `tcp_server.py`: The server-side implementation.
- `tcp_client.py`: The client-side implementation.

## Features
- Connection establishment using a custom three-way handshake.
- Simulated data transmission with basic echo functionality.
- Graceful connection termination.

## How to Run

### 1. Start the Server
Run the server in one terminal:
```bash
python tcp_server.py
