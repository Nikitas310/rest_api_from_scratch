import importlib

from server_core.server_socket import server_socket_run
from server_core import settings
from html_handler.http_response import create_http_response


def runserver(host='127.0.0.1', port=8000):
    get_response = build_middleware_chain()
    server_socket_run(host, port, get_response)


def build_middleware_chain():
    get_response = final_view_handler
    for middleware_path in reversed(settings.MIDDLEWARE):
        module_name, class_name = middleware_path.rsplit('.', 1)
        module = importlib.import_module(module_name)
        middleware_class = getattr(module, class_name)
        get_response = middleware_class(get_response)
    return get_response


def final_view_handler(request,):
    body = 'Connection is good'
    response = create_http_response(
        'HTTP/1.1',
        '200 OK',
        ['Content-Type: text/plain', f'Content-Length: {len(body)}'],
        body
    )
    return response


if __name__ == '__main__':
    runserver()
