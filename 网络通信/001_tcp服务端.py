import socket

'''
服务端的serv_socket只是接收客户端连接，生成client_socket,
服务端有许多client_socket,服务端使用client_socket与对应的客户端通信，而不是使用serv_socket
'''

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 9999))
serversocket.listen(5)
while True:
    clientsocket, addr = serversocket.accept()
    print('连接地址%s' % str(addr))
    msg = '欢迎访问我的服务器'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
serversocket.close()
