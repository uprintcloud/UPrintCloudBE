def getHash(f):
    line=f.readline()
    hash=hashlib.md5()
    while(line):
        hash.update(line)
        line=f.readline()
    return hash.hexdigest()
def unique(fileName,content):  # fileName: 传入的文件名
    fileName=getHash(content)
    return fileName  # return 绝对唯一的文件名

def fileName2key(fileName):  # fileName: 绝对唯一的文件名
    key = fileName
    return key  # 8位密钥，前四位为日期，后四位随机
