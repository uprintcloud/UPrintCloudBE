from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(verbose_name='用户昵称', max_length=32)
    file_count = models.IntegerField(verbose_name='文件数量', default=0)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class RabbitMQNode(models.Model):
    url = models.CharField(verbose_name='节点地址', max_length=32, primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=10)
    password = models.CharField(verbose_name='密码', max_length=32)

    class Meta:
        verbose_name = '节点'
        verbose_name_plural = '节点'


class Client(models.Model):
    id = models.CharField(verbose_name='终端识别号', max_length=11, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='所属用户')
    rabbitmq_node = models.ForeignKey(RabbitMQNode, on_delete=models.PROTECT, verbose_name='依赖节点')

    class Meta:
        verbose_name = '终端'
        verbose_name_plural = '终端'


class Job(models.Model):
    id = models.CharField(verbose_name='任务编号', max_length=30, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='所属用户')
    file = models.FileField(verbose_name='文件', upload_to='static/usr/uploads/files/%Y/%m/%d/')
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    finished = models.BooleanField(verbose_name='已经打印', default=False)
    finished_date = models.DateTimeField(verbose_name='打印日期', auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='打印终端', null=True)

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务'
        ordering=['-create_date']



