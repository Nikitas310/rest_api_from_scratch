from .views import registration


def deliver(request, depth):
    path = request.path.split('/')[depth]
    if path == 'registration':
        registration(request)
