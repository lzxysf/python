import socket
from multiprocessing import Process
import re
import os


class WSGIServer(object):
    def __init__(self, serv_addr):
        self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv_sock.bind(serv_addr)
        self.serv_sock.listen(1000)

    def serve_forever(self):
        while True:
            cli_sock, cli_addr = self.serv_sock.accept()
            p = Process(target=self.handle_client, args=(cli_sock,))
            p.start()
            cli_sock.close()

    def handle_client(self, cli_sock):
        request_data = cli_sock.recv(1024)
        request_header_lines = request_data.splitlines()
        for line in request_header_lines:
            print(line)

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

        cli_sock.send((response_header + response_body).encode("utf-8"))
        cli_sock.close()

# 根目录
# 类的内部是可以访问到http_root_dir的，不用加global
# 内部不加global时，函数里可以访问到，但是不能对其进行修改
# 加了golbal就能对其进行修改了
http_root_dir = os.getcwd()
serv_addr = (HOST,PORT) = ('',7788)

def makeserver(serv_addr):
    server = WSGIServer(serv_addr)
    return server

def main():
    httpd = makeserver(serv_addr)
    print('serving http on port',PORT)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
