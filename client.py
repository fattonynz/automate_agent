import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        with socket.create_connection((self.host, self.port)) as sock:
            sock.sendall(b"Hello, server!")
            data = sock.recv(1024)
            print(f"Received from server: {data.decode()}")

client = Client(host="3.86.198.38", port=443)
client.connect()
