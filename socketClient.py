import socket
host = "127.0.0.1"
port = 2121
with socket.socket() as soket:
    soket.connect((host, port))
    soket.sendall(b"Hey Cyber!")
    data = soket.recv(1024)
print(data)
