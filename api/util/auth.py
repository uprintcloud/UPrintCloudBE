from Data import models as data


def get_username(token):
    return token.split(',')[0]


def get_password(token):
    return token.split(',')[1]


def token_auth(token):
    username = get_username(token)
    try:
        user = data.User.objects.get(username)
    except data.models.ObjectDoesNotExist:
        return False
    else:
        return user.check_password(get_password(token))


def token_generator(user):
    return "%s,%s" % (user.username, user.password)
