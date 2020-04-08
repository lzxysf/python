import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bindAddr = ('', 7788)
s.bind(bindAddr)
recvdata = s.recvfrom(1024)
print(recvdata)
s.close()
