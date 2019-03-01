from django.shortcuts import render, HttpResponse
from requests import get
import os

# Create your views here.


def index(requests):
    if requests.method == 'GET':
        file_name = requests.GET.get('file', -1)
        if file_name != -1:
            url = 'http://127.0.0.1:8001/request/download/%s' % file_name
            req = get(url)
            with open('usr%sbuf.pdf' % (os.path.sep), 'wb') as file:
                file.write(req.content)
    return HttpResponse(404)
