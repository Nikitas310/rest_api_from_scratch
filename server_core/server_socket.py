import socket

from html_handler.http_response import create_http_response
from html_handler.http_parser import parse_http_request
from .urls import deliver
from requests.my_requests import Request


def server_socket_run(host, port, get_response):
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)

    server_socket.settimeout(1)

    print(f"Server running on {host}:{port}. Press Ctrl+C to stop.")

    try:
        while True:
            try:
                conn, addr = server_socket.accept()
                print("Connected by", str(addr))
            except socket.timeout:
                continue
            with conn:
                while True:
                    data = conn.recv(1024).decode()
                    if not data:
                        break

                    request = Request(*parse_http_request(data))
                    response = get_response(request)

                    conn.send(response.encode())

    except KeyboardInterrupt:
        print("\n[!] Server interrupted by user. Shutting down gracefully.")
    finally:
        server_socket.close()


