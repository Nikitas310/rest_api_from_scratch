from server_core.server_socket import server_socket_run


def runserver(host='127.0.0.1', port=8000):
    server_socket_run(host, port)


if __name__ == '__main__':
    runserver()