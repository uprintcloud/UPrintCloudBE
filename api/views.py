from django.shortcuts import HttpResponse, Http404
from django.http import FileResponse
from django.utils.http import urlquote
from django.contrib import auth
from Data import models as data
from util import rabbitmq
import time
import filetype


def upload(requests):
    if requests.method == 'POST':
        file = requests.FILES.get('file', None)

        if 'username' not in requests.POST:
            return HttpResponse('Please login first')

        if not file:
            return HttpResponse('Empty file')

        if filetype.guess(file).EXTENSION != 'pdf':
            return HttpResponse('Wrong type')

        username = requests.POST['username']
        date = time.strftime("%Y%m%d%H%M%S", time.localtime())
        user = data.User.objects.get(username=username)
        user.file_count = user.file_count + 1
        user.save(update_fields=['file_count'])
        job = data.Job(
            id=date + username,
            user=user,
            file=file,
            create_date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        )
        job.save()
        return HttpResponse(date + username)
    raise Http404


def request(requests):
    if requests.method == 'GET':
        if 'job_id' in requests.GET:
            job = data.Job.objects.get(id=requests.GET['job_id'])
            client = data.Client.objects.get(id=requests.GET['client_id'])
            if job.finished:
                raise Http404

            rabbitmq.push(
                uri=client.rabbitmq_node.url,
                username=client.rabbitmq_node.username,
                passwd=client.rabbitmq_node.password,
                content=requests.GET['job_id'],
                queue_name=client.id
            )
            job.client = client
            job.save(update_fields=['client'])
            return HttpResponse('Success')

    raise Http404


def download(requests):
    if requests.method == 'GET':
        if 'job_id' in requests.GET:
            job = data.Job.objects.get(id=requests.GET['job_id'])
            response = FileResponse(job.file)
            response['Content-Type'] = 'application/pdf'
            response["Content-Disposition"] = "attachment;filename*=UTF-8''%s" % urlquote(job.file.name.split('/')[-1])
            job.finished = True
            job.finished_date= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            job.save(update_fields=['finished', 'finished_date'])
            return response

    raise Http404


def login(requests):
    username = requests.POST['username']
    password = requests.POST['password']
    if '@' not in username:
        try:
            user = data.User.objects.get(username=username)
        except data.models.ObjectDoesNotExist:
            return HttpResponse('fail')
        else:
            username = user.email
    user = auth.authenticate(requests, email=username, password=password)
    if user is not None:
        auth.login(requests, user)
        return HttpResponse(user.username)
    return HttpResponse('fail')


def join(requests):
    email = requests.POST['email']
    nickname = requests.POST['nickname']
    password = requests.POST['password']
    try:
        data.User.objects.get(email=email)
    except data.models.ObjectDoesNotExist:
        user = data.User.objects.create_user(email=email, nickname=nickname, password=password)
        user.save()
        return HttpResponse('success')
    return HttpResponse('duplicated')
