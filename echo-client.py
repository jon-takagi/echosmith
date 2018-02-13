import socket
s = socket.socket()
host = socket.gethostname()
port = 42069

s.connect((host, port))
print(str(s.recv(1024)))
s.close()

