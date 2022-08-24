import configparser
import os
import pandas
import pymysql
def entry():
    file=configparser.ConfigParser()
    file.read('entry.ini',encoding='utf-8')
    dbs='entry'
    which_server=file.get(dbs,'which_server')
    which_db=file.get(dbs,'which_db')
    return which_server,which_db
def Ser():
    which_server=entry()[0]
    file=configparser.ConfigParser()
    file.read('server.conf',encoding='utf-8')
    ip=file.get(which_server,'ip')
    port=file.get(which_server,'port')
    host='http://'+ip+':'+port
    return host
def Db():
    which_db=entry()[1]
    dbfile=configparser.ConfigParser()
    dbfile.read('db.conf',encoding='utf-8')
    host=dbfile.get(which_db,'host')
    port=dbfile.get(which_db,'port')
    user=dbfile.get(which_db,'user')
    password=dbfile.get(which_db,'password')
    db=dbfile.get(which_db,'db')
    dbs={'host':host,'port':int(port),'user':user,'password':password,'db':db}
    return dbs
def read_sql(sqlfile=[]):
    sqls=[]
    if len(sqlfile)==0:
        sqlfile=[file for file in os.listdir('.') if file.endswith('.txt')]
    for file in sqlfile:
        data=open(file,'r',encoding='utf-8')
        for row in data:
            if len(row.strip())>0:
                sqls.append(row.strip())
        data.close()
    return sqls
def db_info():
    dbinfo=Db()
    conn=pymysql.connect(**dbinfo)
    return conn
def inti_db(sqlfils=[]):
    sqls=read_sql(sqlfils)
    conn=db_info()
    cur=conn.cursor()
    for sql in sqls:
        cur.execute(sql)
    conn.commit()
    conn.close()

def read_case(excefile,clous=[]):
    if len(clous)==0:
        file=pandas.read_excel(excefile)
    else:
        file=pandas.read_excel(excefile,usecols=clous)
        case=file.values.tolist()
        return case
print(read_case('注册接口验证.xls'))



