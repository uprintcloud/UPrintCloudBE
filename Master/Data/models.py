from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Users(AbstractBaseUser):
    account = models.CharField(verbose_name='账号', max_length=10, primary_key=True)
    user_name = models.CharField(verbose_name='用户名', max_length=30)
    file_count = models.IntegerField(verbose_name='文件数量')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户集合'


class Jobs(models.Model):
    jobId = models.CharField(verbose_name='任务编号', max_length=24, primary_key=True)
    account = models.CharField(verbose_name='所属账号', max_length=10)
    file = models.FileField(verbose_name='文件', upload_to='files/%Y/%m/%d/')
    create_date = models.DateField(verbose_name='创建日期', auto_now_add=True)
    finished = models.BooleanField(verbose_name='已经打印', default=False)
    finished_date = models.DateField(verbose_name='打印日期', null=True)
    finished_locate = models.CharField(verbose_name='打印地点', max_length=128, null=True)

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务集合'
        ordering=['-create_date']

