import socket
s = socket.socket()
host = socket.gethostname()
port = 42069
s.bind(('0.0.0.0', port))

s.listen(5)
while True:
	client, addr = s.accept()
	while True:
		data = client.recv(2048)
		if data == b'quit\r\n':
			client.shutdown(1)
			client.close()
		else:
			client.send(data)
			print(data)
