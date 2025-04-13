def registration(request):
    data = request.body
    username = data.get('username')
    password = data.get('password')
    print(username, password)