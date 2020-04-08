import socket
from multiprocessing import Process
import re
import os


def handle_client(cli_sock):
    request_data = cli_sock.recv(1024)
    request_header_lines = request_data.splitlines()
    for line in request_header_lines:
        print(line)

    # 根目录
    http_root_dir = os.getcwd()

    # 请求头的第一行，里面包含请求路径，使用正则表达式将这个路径提取出来
    # GET /index.html HTTP/1.1
    http_method_line = request_header_lines[0].decode('utf-8')
    file_path = re.match(r'\w+\s+(/\S*)\s', http_method_line).group(1)
    if file_path == '/':
        file_path = http_root_dir + '/index.html'
    else:
        file_path = http_root_dir + file_path

    try:
        f = open(file_path, 'rb')
    except IOError:
        response_header = "HTTP/1.1 404 NOT FOUND\r\n"
        response_header += "\r\n"
        response_body = "sorry,file not found"
    else:
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "\r\n"
        response_body = f.read().decode("utf-8")

    cli_sock.send((response_header+response_body).encode("utf-8"))
    cli_sock.close()


def main():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_sock.bind(('', 7788))
    serv_sock.listen(100)
    while True:
        cli_sock, cli_addr = serv_sock.accept()
        p = Process(target=handle_client, args=(cli_sock,))
        p.start()
        cli_sock.close()


if __name__ == '__main__':
    main()
