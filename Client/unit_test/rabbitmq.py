from util import rabbitmq

if __name__ == '__main__':
    username = 'master'
    passwd = 'admin'
    uri = 'debian-docker'
    rabbitmq.listen(uri, username, passwd, '01234567890')
