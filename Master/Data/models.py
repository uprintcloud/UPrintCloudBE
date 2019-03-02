from django.db import models


class User(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=10, primary_key=True)
    password = models.CharField(verbose_name='密码', max_length=128)
    nickname = models.CharField(verbose_name='用户昵称', max_length=30)
    file_count = models.IntegerField(verbose_name='文件数量', default=0)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Job(models.Model):
    job_id = models.CharField(verbose_name='任务编号', max_length=30, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='所属用户')
    file = models.FileField(verbose_name='文件', upload_to='usr/uploads/files/%Y/%m/%d/')
    create_date = models.DateField(verbose_name='创建日期', auto_now_add=True)
    finished = models.BooleanField(verbose_name='已经打印', default=False)
    finished_date = models.DateField(verbose_name='打印日期', null=True)
    finished_locate = models.CharField(verbose_name='打印地点', max_length=128, null=True)

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务'
        ordering=['-create_date']


