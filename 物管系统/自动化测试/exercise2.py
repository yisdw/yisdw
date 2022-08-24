import configparser
file=configparser.ConfigParser()
file.read('db.conf',encoding='utf-8')
dbs='exam-192-db'
host=file.get(dbs,'host')
port=file.get(dbs,'port')
user=file.get(dbs,'user')
password=file.get(dbs,'password')
db=file.get(dbs,'db')
print(host,port,user,password,db)
