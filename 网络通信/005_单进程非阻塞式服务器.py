from socket import *


def main():
    serv_sock = socket(AF_INET, SOCK_STREAM)
    serv_sock.bind(('', 7070))
    serv_sock.listen()
    serv_sock.setblocking(False)

    client_info_lists = []

    while True:
        try:
            client_info = serv_sock.accept()
        except Exception as e:
            pass
        else:
            print('有新的连接', client_info[1])
            client_info[0].setblocking(False)
            client_info_lists.append(client_info)

        client_info_for_del_lists = []

        for client_info in client_info_lists:
            try:
                data = client_info[0].recv(1024)
                if len(data) > 0:
                    print('收到{}的数据:{}'.format(client_info[1], data))
                else:
                    print('{}关闭'.format(client_info[1]))
                    client_info[0].close()
                    client_info_for_del_lists.append(client_info)
            except Exception as e:
                pass

        for client_info in client_info_for_del_lists:
            client_info_lists.remove(client_info)


if __name__ == '__main__':
    main()
