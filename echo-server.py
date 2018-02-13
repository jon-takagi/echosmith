import socket
s = socket.socket()
host = socket.gethostname()
port = 42069
s.bind((host, port))

s.listen(5)
while True:
	client, addr = s.accept()
	print("connection from: ", addr)
	client.send(b'ping')
	client.close()
