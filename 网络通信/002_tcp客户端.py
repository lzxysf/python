import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9999))
msg = s.recv(1024)
s.close()
print(msg.decode('utf-8'))
