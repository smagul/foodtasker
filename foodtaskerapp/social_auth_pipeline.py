from foodtaskerapp.models import Customer, Driver


def create_user_by_type(backend, user, request, response, *args, **kwargs):
    if backend.name == 'facebook':
        avatar = 'https://graph.facebook.com/%s/picture?type=large' % response['id']

    if request['user_type'] == "driver" and not Driver.objects.filter(user_id=user.id):
        Driver.objects.create(user_id=user.id, avatar=avatar)
    elif not Customer.objects.create(user_id=user.id, avatar=avatar):
        Customer.objects.create(user_id=user.id, avatar=avatar)