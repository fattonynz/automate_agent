import socket
import ssl

class SecureClient:
    def __init__(self, host, port, certfile, keyfile, cafile):
        self.host = host
        self.port = port
        self.certfile = certfile
        self.keyfile = keyfile
        self.cafile = cafile

    def connect(self):
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_cert_chain(certfile=self.certfile, keyfile=self.keyfile)
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile=self.cafile)
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        with socket.create_connection((self.host, self.port)) as sock:
            with context.wrap_socket(sock, server_hostname=self.host) as ssock:
                cert = ssock.getpeercert()
                if not cert:
                    print("Server did not provide a certificate.")
                    return

                # Verify the server certificate here
                # ...

                ssock.sendall(b"Hello, server!")
                data = ssock.recv(1024)
                print(f"Received from server: {data.decode()}")

client = SecureClient(host="localhost", port=443, certfile="client.crt", keyfile="client.key", cafile="ca.crt")
client.connect()
