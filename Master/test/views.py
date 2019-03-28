from django.shortcuts import HttpResponse, render, redirect
from Data import models


def init(requests):
    user = models.User(username='1607020115', email='mail@mail.com', nickname='Lucien Shui')
    user.set_password('123456')
    user.save()
    node = models.RabbitMQNode(url='debian-docker', username='master', password='admin')
    node.save()
    models.Client(id='01234567890', user=user, rabbitmq_node=node).save()
    return HttpResponse('Success')


def upload(requests):
    return render(requests, 'upload.html')


def index(requests):
    return render(requests, 'index.html')


def join(requests):
    return render(requests, 'join.html')


def login(requests):
    if requests.user.is_authenticated:
        return redirect('/')
    return render(requests, 'login.html')
