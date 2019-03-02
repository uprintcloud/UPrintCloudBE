from django.shortcuts import render, HttpResponse, Http404
from Data import models as data
from util import rabbitmq
import time


def upload(requests):
    if requests.method == 'POST':
        file = requests.FILES.get('file', None)
        if not file:
            return HttpResponse('Empty file')

        username = '1607020115'
        date = time.strftime("%Y%m%d%H%M%S", time.localtime())
        user = data.User.objects.get(username=username)
        user.file_count = user.file_count + 1
        user.save(update_fields=['file_count'])
        job = data.Job(
            job_id=date + username,
            user=user,
            file=file,
        )
        job.save()

    return HttpResponse('Success!')


def request(requests):
    if requests.method == 'GET':
        if 'job_id' in requests.GET:
            job = data.Job.objects.get(job_id=requests.GET['job_id'])
            rabbitmq.push(uri='debian-docker', username='master', passwd='admin', content='127.0.0.1:8000/%s' % job.file.url, queue_name=requests.GET['client_id'])
            return HttpResponse(job.file.url)
    raise Http404


