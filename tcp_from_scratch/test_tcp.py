"""
test_tcp.py

Tests the TCP server and client functionality.
"""

import threading
import time
import tcp_server
import tcp_client

def test_tcp():
    # Start the server in a separate thread
    server_thread = threading.Thread(target=tcp_server.start_server, kwargs={"port":5555}, daemon=True)
    server_thread.start()

    # Give the server some time to start
    time.sleep(1)

    # Run the client
    tcp_client.tcp_client(server_host="127.0.0.1", server_port=5555)

if __name__ == "__main__":
    test_tcp()
