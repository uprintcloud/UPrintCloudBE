import hashlib
import random
import string
from Request.models import Key


def getHash(f):
    line = f.readline()
    hash_code = hashlib.md5()
    while (line):
        hash_code.update(line)
        line = f.readline()
    return hash_code.hexdigest()


def unique(content):  # file_name: 传入的文件名
    file_name = getHash(content)
    return file_name  # return 绝对唯一的文件名


def file_name2key(password):
    buf = string.digits
    former = ''.join(random.choice(buf) for _ in range(4))
    key = former + password
    while Key.objects.filter(key=key, is_print=False).count():
        former = ''.join(random.choice(buf) for _ in range(4))
        key = former + password
    return key
