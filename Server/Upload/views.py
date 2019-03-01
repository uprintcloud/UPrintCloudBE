from django.shortcuts import render, HttpResponse
import os
from . import lib

# Create your views here.


def index(requests):
    return render(requests, 'Upload/index.html')


def submit(requests):
    if requests.method == 'POST':
        file = requests.FILES.get('file', None)  # 抓取文件
        if not file:  # 如果文件为空
            return HttpResponse("No file for upload")

        path = open(  # 文件的保存路径 usr/uploads
            os.path.join('.%susr%suploads' % (os.path.sep, os.path.sep), file.name)
            , 'wb+')
        for chunk in file.chunks():  # 文件分块
            path.write(chunk)
        path.close()
        key = lib.file_name2key(lib.unique(file.name))  # 将文件哈希为key
        data = {
            'key': key,
        }
        return render(requests, 'Upload/success.html', data)
