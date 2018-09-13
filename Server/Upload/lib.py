import random
import string
from Request.models import Key
def getHash(f):
    line=f.readline()
    hash=hashlib.md5()
    while(line):
        hash.update(line)
        line=f.readline()
    return hash.hexdigest()
def unique(fileName, content):  # fileName: 传入的文件名
    fileName=getHash(content)
    return fileName  # return 绝对唯一的文件名

def fileName2key(fileName, password):
    buf = string.digits
    former = ''.join(random.choice(buf) for _ in range(4))
    key = former + password
    while Key.objects.filter(key=key, is_print=False).count():
        former = ''.join(random.choice(buf) for _ in range(4))
        key = former + password
    return key
