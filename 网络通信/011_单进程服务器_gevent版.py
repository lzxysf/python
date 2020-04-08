import socket
import gevent
from gevent import monkey

def handle_client(cli_sock):
    while True:
        data = cli_sock.recv(1024)
        if data:
            print('收到数据', data)
        else:
            cli_sock.close()
            # 此处必须有break,即cli_sock关闭后不能再对它循环进行操作了
            break


def server():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.bind(('', 7070))
    serv_sock.listen(1000)
    while True:
        cli_sock, cli_addr = serv_sock.accept()
        # handle_client(cli_sock)
        gevent.spawn(handle_client, cli_sock)


if __name__ == '__main__':
    monkey.patch_all()
    server()
