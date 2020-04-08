'''
在多路复用的模型中，比较常用的有select模型和epoll模型。这两个都是系统接口，由操作系统提供。

网络通信被Unix系统抽象为文件的读写，通常是一个设备，由设备驱动程序提供，驱动可以知道自身的数据是否可用。支持阻塞操作的设备驱动通常会实现一组自身的等待队列，如读/写等待队列用于支持上层(用户层)所需的block或non-block操作。设备的文件的资源如果可用（可读或者可写）则会通知进程，反之则会让进程睡眠，等到数据到来可用的时候，再唤醒进程。

([readable],[writealbe],[exceptional]) = select([rlist],[wlist],[xlist])
select中三个参数是三个列表，列表的元素是socket
将socket加入第一个列表可在socket可读时返回，将socket加入第二个列表可在可写时返回，将socket加入第三个列表可在有异常时返回
返回值是一个包含三个列表的元组，分别返回当前可读、可写、有异常的socket
'''

'''
优点
select目前几乎在所有的平台上支持，其良好跨平台支持也是它的一个优点。

缺点
select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024，可以通过修改宏定义甚至重新编译内核的方式提升这一限制，但是这样也会造成效率的降低。

一般来说这个数目和系统内存关系很大，具体数目可以cat /proc/sys/fs/file-max察看。32位机默认是1024个。64位机默认是2048.

对socket进行扫描时是依次扫描的，即采用轮询的方法，效率较低。

当套接字比较多的时候，每次select()都要通过遍历FD_SETSIZE个Socket来完成调度，不管哪个Socket是活跃的，都遍历一遍。这会浪费很多CPU时间。
'''

from socket import *
import select


def main():
    serv_sock = socket(AF_INET, SOCK_STREAM)
    serv_sock.bind(('', 8989))
    serv_sock.listen(1000)
    serv_sock.setblocking(False)

    input_lists = [serv_sock]

    while True:
        readable, writeable, exceptional = select.select(input_lists, [], [])
        for sock in readable:
            # 有客户端连接
            if sock == serv_sock:
                client_sock, client_addr = serv_sock.accept()
                client_sock.setblocking(False)
                input_lists.append(client_sock)
            # 有客户端数据到达
            else:
                data = sock.recv(1024)
                if data:
                    print('客户端有数据到达', sock.getpeername(), str(data))
                    sock.send(data)
                else:
                    sock.close()
                    input_lists.remove(sock)


if __name__ == '__main__':
    main()
