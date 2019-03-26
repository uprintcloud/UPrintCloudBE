from django.shortcuts import HttpResponse
from Data import models


def index(requests):
    user = models.User(username='1607020115', email='mail@mail.com', nickname='Lucien Shui', password='123456')
    user.save()
    node = models.RabbitMQNode(url='debian-docker', username='master', password='admin')
    node.save()
    models.Client(id='01234567890', user=user, rabbitmq_node=node).save()
    return HttpResponse('Success')
