import socket
import ssl

class SecureClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        with socket.create_connection((self.host, self.port)) as sock:
            with context.wrap_socket(sock, server_hostname=self.host) as ssock:
                ssock.sendall(b"Hello, server!")
                data = ssock.recv(1024)
                print(f"Received from server: {data.decode()}")

client = SecureClient(host="localhost", port=888)
client.connect()
