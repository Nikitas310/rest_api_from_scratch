from users.urls import deliver as users_deliver


def deliver(request):
    path = request.path.split('/')[1]
    if path == 'users':
        users_deliver(request, 2)


urlpatterns = ['users', ]