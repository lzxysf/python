from socket import *


def main():
    client_socket_lists = []

    for i in range(10):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 7070))
        client_socket_lists.append(client_socket)

    for client_socket in client_socket_lists:
        client_socket.send('i am client'.encode('utf-8'))


if __name__ == '__main__':
    main()
