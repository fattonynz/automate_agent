import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        with socket.create_connection((self.host, self.port)) as sock:
            print(f"Connected to {self.host}:{self.port}")
            sock.sendall(b"Hello, server!")
            print("Sent message to server")
            data = sock.recv(1024)
            print(f"Received from server: {data.decode()}")
            
client = Client(host="3.86.198.38", port=443)
try:
    client.connect()
except Exception as e:
    print(f"Error: {e}")