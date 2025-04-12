def create_http_response(http_version, http_code, headers, body):

    headers_response = '\r\n'.join(headers)

    response = f'{http_version} {http_code}\r\n{headers_response}\r\n\r\n{body}'

    return response

