import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        with socket.create_connection((self.host, self.port)) as sock:
            print(f"Connected to {self.host}:{self.port}")
            sock.sendall(b"{workflow_id:1}")
            print("Sent message to server")
            data = sock.recv(1024)
            print(f"Received from server: {data.decode()}")
            
client = Client(host="3.86.198.38", port=6000)
try:
    client.connect()
except Exception as e:
    print(f"Error: {e}")