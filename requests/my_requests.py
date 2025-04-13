import json


class Request:

    def __init__(self, http_method, path, http_version, headers, body):
        self.method = http_method
        self.path = path
        self.http_version = http_version
        self.headers = headers
        self.body = self.set_body(body)
        self.cookies = self.set_cookies()
        self.session = None


    def __repr__(self):
        return f"<Request {self.method} {self.path}>"

    def set_body(self, body):
        if self.headers.get('content-type') == 'application/json':
            body = json.loads(body)
            return body
        else:
            raise Exception('Invalid content type')

    def set_cookies(self):
        cookies = self.headers.get('cookie').split(';')
        if cookies:
            cookies = dict(value.strip().split('=') for value in cookies)
        return cookies

