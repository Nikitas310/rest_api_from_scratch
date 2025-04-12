def parse_http_request(request):
    data = request.split('\r\n')
    start_line = data[0].split(' ')
    try:
        http_method, path, http_version = start_line
    except ValueError:
        return None

    headers, end_headers_index = get_headers(data[1:])

    body = ''.join(data[end_headers_index + 2:])
    return http_method, path, http_version, headers, body


def parse_http_response(response):
    data = response.split('\r\n')
    start_line = data[0].split(' ')
    try:
        http_version, http_code = start_line[0], int(start_line[1])
    except ValueError:
        return None

    headers, end_headers_index = get_headers(data[1:])

    body = ''.join(data[end_headers_index + 2:])
    return http_version, http_code, headers, body


def get_headers(data):
    end_headers_index = None
    headers = {}
    for i, line in enumerate(data):
        if line == '':
            end_headers_index = i
            break
        header, value = line.split(':', 1)
        headers[header.lower()] = value.strip()
    return headers, end_headers_index
