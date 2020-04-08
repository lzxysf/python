import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sendAddr = ('127.0.0.1', 7788)
sendData = 'helloworld'
s.sendto(sendData.encode('utf-8'), sendAddr)
s.close()
