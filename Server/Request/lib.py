import random
import string
import shutil
import os
import requests
from .models import Key
from django.db.models import ObjectDoesNotExist


def strRand():  # 生成20位随机字符串
    buf = string.ascii_letters + string.digits
    return ''.join(random.choice(buf) for _ in range(20))


def key2fileName(key):  # 将key转化为fileName
    try:
        filename = Key.objects.get(key=key, is_print=False).filename
    except ObjectDoesNotExist:
        filename = None
    return filename


def getFile(key):  # 获得某个文件的临时拷贝，并移动至usr/downloads目录下
    filename = key2fileName(key)  # 将key转化为fileName
    sep = os.path.sep
    if not os.path.exists('usr%suploads%s%s' % (sep, sep, filename)):
        return -1
    dst = '%s.%s' % (strRand(), filename.split('.')[-1])
    shutil.copyfile('usr%suploads%s%s' % (sep, sep, filename), 'usr%sdownloads%s%s' % (sep, sep, dst))
    return dst  # 临时拷贝的文件名


def sendRequest(url, file):  # 向printer发送打印请求
    requests.get("%s?file=%s" % (url, file))
