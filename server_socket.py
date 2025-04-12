import socket

from http_parser import parse_http_request
from http_response import create_http_response


def main():
    host = "localhost"
    port = 8000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(5)
    conn, addr = server_socket.accept()
    print("Connected by", str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        http_method, path, http_version, headers, body = parse_http_request(data)

        data = create_http_response(
            'HTTP/1.1',
            '200 OK',
            ['Content-Type: text/plain',f'Content-Length: {len('Connection is good')}'],
            'Connection is good')
        conn.send(data.encode())
    conn.close()




if __name__ == "__main__":
    main()
