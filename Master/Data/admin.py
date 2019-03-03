from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.RabbitMQNode)
admin.site.register(models.Client)
admin.site.register(models.Job)

