import  configparser
file=configparser.ConfigParser()
file.read('server.conf',encoding='utf-8')
ip=file.get('exam-192','ip')
port=file.get('exam-192','port')
host='http://'+ip+":"+port
print(host)