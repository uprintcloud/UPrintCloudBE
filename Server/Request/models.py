from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Key(models.Model):
    key = models.CharField(max_length=17)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    upload_date = models.DateTimeField(auto_now_add=True)
    print_date = models.DateTimeField(auto_now=True)
    filename = models.CharField(max_length=50)
    is_print = models.BooleanField(default=False)

    def __str__(self):
        return '<Key: %s>' %self.key