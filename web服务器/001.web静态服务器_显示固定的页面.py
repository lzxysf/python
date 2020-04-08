import socket
from multiprocessing import Process


def handle_client(cli_sock):
    request_data = cli_sock.recv(1024)
    request_header_lines = request_data.splitlines()
    for line in request_header_lines:
        print(line)

    # 响应头和响应体之间有两个\r\n隔开，这是标志，看到两个\r\n就知道下面就是响应体了
    response_header = "HTTP/1.1 200 OK\r\n"
    response_header += "\r\n"
    response_body = "<h1>hello world<h1>"
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
