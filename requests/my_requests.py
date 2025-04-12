class Request:

    def __init__(self, http_method, path, http_version, headers, body):
        self.method = http_method
        self.path = path
        self.http_version = http_version
        self.headers = headers
        self.body = body

    def __repr__(self):
        return f"<Request {self.method} {self.path}>"

