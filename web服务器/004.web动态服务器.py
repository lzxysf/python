import socket
from multiprocessing import Process
import re
from WebFramework import app


class HTTPServer(object):
    def __init__(self, serv_addr):
        self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv_sock.bind(serv_addr)
        self.serv_sock.listen(1000)
        self.response_header = ''
        self.response_body = ''

    def set_app(self, application):
        self.application = application

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

        http_method_line = request_header_lines[0].decode('utf-8')
        file_path = re.match(r'\w+\s+(/\S*)\s', http_method_line).group(1)
        env = {
            'PATH_INFO':file_path
        }
        self.response_body = self.application(env, self.start_response)
        cli_sock.send((self.response_header + '\r\n' + self.response_body).encode('utf-8'))
        cli_sock.close()

    def start_response(self, state, headers):
        response_header = "HTTP/1.1 " + state + "\r\n"
        for header in headers:
            response_header += "%s: %s\r\n" % header
        self.response_header = response_header


serv_addr = (HOST,PORT) = ('',7788)

def makeserver(serv_addr):
    server = HTTPServer(serv_addr)
    return server

def main():
    httpd = makeserver(serv_addr)
    print('serving http on port',PORT)
    httpd.set_app(app)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
