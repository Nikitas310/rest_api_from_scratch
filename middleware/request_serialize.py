from html_handler.http_parser import parse_http_request
from requests.my_requests import Request
from middleware.middleware_manager import BaseMiddleware
import json


class RequestSerializerMiddleware(BaseMiddleware):

    def __call__(self, request):
        return self.get_response(request)


class SessionMiddleware(BaseMiddleware):

    def __call__(self, request):
        sessionid = request.cookies.get('sessionid')
        if sessionid:
            request.session = self.load_session(sessionid)
        else:
            sessionid = '1234567890'
        response = super().__call__(request)
        return response

    def load_session(self, sessionid):
        with open(f'./session.json', 'r') as f:
            session_file = json.load(f)
            session = session_file.get(sessionid)
            return session
