'''
没有最大并发连接的限制，能打开的fd(文件描述符)的上限远大于1024

效率提升，不是轮询的方式，不会随着fd数目的增加效率下降。只有活跃可用的fd才会调用callback函数；即epoll最大的优点就在于它只管你“活跃”的连接，而跟连接总数无关，因此在实际的网络环境中，epoll的效率就会远远高于select

select和epoll在操作上的区别是
select是将socket加入到函数select.select()中
epoll是将socket的文件描述符fd加入到函数epoll.register()中


EPOLLIN （可读）
EPOLLOUT （可写）
EPOLLET （ET模式）
epoll对文件描述符的操作有两种模式：LT（level trigger，水平触发）和ET（edge trigger，边缘触发）。LT模式是默认模式，不用专门设置

LT模式与ET模式的区别如下：
LT模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序可以不立即处理该事件。下次调用epoll时，会再次响应应用程序并通知此事件。
ET模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序必须立即处理该事件。如果不处理，下次调用epoll时，不会再次响应应用程序并通知此事件。
'''

import select
from socket import *

def main():
    serv_sock = socket(AF_INET, SOCK_STREAM)
    serv_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serv_sock.bind(('', 7070))
    serv_sock.listen(1000)

    epoll = select.epoll()

    connections = {}
    address = {}

    # print(serv_sock.fileno())
    # print(select.EPOLLIN)
    # print(select.EPOLLOUT)
    # print(select.EPOLLET)
    # print(select.EPOLLIN|select.EPOLLET)

    epoll.register(serv_sock.fileno(), select.EPOLLIN|select.EPOLLET)

    while True:
        # epoll进行扫描的地方，未指定超时时间则为阻塞等待
        epoll_list = epoll.poll()
        for fd,events in epoll_list:
            # serv_sock有数据可读，即有新的客户端连接
            if fd == serv_sock.fileno():
                client_sock,client_addr = serv_sock.accept()
                connections[client_sock.fileno()] = client_sock
                address[client_sock.fileno()] = client_addr
                epoll.register(client_sock.fileno(), select.EPOLLIN|select.EPOLLET)
            
            # client_sock有数据可读，即服务器受到了客户端数据
            # 此处不能用else,具体原因待查证
            elif events == select.EPOLLIN:
                client_sock = connections[fd]
                client_addr = address[fd]
                data = client_sock.recv(1024)
                if data:
                    print('recv from {},data is {}'.format(client_addr, data))
                else:
                    epoll.unregister(fd)
                    client_sock.close()
                    print('{} closed!'.format(client_addr))

if __name__ == '__main__':
    main()
