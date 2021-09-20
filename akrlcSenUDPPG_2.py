#!/usr/bin/env python3
from socket import *
import time
import os
import os.path
from os import path
import psycopg2
from datetime import datetime

def saveAWSrds(tstz, data):
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="c3120387",
        host="acrylicsensortest.co80j7fua52a.rds.cn-northwest-1.amazonaws.com.cn",
        port='5432'
    )
    cursor = conn.cursor()
    # get current time
    datetime_utc = datetime.now()
    print(datetime_utc)
    # sql语句 建表
    sql ="""INSERT INTO wearData (ts, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    params = (tstz, data[0], data[1], data[2], data[3], data[4], data[5], data[6], \
            data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], \
            data[15], data[16], data[17], data[18], data[19])
    # 执行语句
    cursor.execute(sql,params)
    print("data inserted into table AWS RDS successfully")
    # 事物提交
    conn.commit()
    # 关闭数据库连接
    conn.close()


def saveLocal(data):
    timer = time.ctime()
    # Converting the string to a time object
    t_obj = time.strptime(timer)
    # Transforming the time object to a timestamp
    form_t = time.strftime("%Y-%m-%d_%H-%M-%S", t_obj)
    fl2wrt = open('tmp.txt', 'w')
    #处理数据
    barr = bytearray(20)
    strarr = []
    cn = 0
    for byts in data:
        barr[cn] = byts
        print(byts)
        strarr.append(byts)
        cn += 1
    
    for elem in strarr:
        fl2wrt.write(str(elem) + "\n")
    fl2wrt.close()

    cpath = os.getcwd()
    # If the file already exists, skip renaming
    if path.exists(form_t + '.txt'):
        print("file already exists, skip renaming")
    else:
        os.rename(cpath +'/tmp.txt',  cpath + '/' + form_t + '.txt' )
    print("data saved locally successfully")
    return

def wtPGDB(tstz, data):
    conn = psycopg2.connect(database="AcrylicSSDB_test", user="postgres", password="354877", host="127.0.0.1", port="5432")
    # 获得游标对象
    cursor = conn.cursor()
    # get current time
    datetime_utc = datetime.now()
    print(datetime_utc)
    # sql语句 建表
    sql ="""INSERT INTO wearData (ts, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    params = (tstz, data[0], data[1], data[2], data[3], data[4], data[5], data[6], \
            data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], \
            data[15], data[16], data[17], data[18], data[19])
    # 执行语句
    cursor.execute(sql,params)
    print("data inserted into table wearData successfully")
    # 事物提交
    conn.commit()
    # 关闭数据库连接
    conn.close()

def main():
    host = ''
    port = 10088 #接口必须一致
    bufsize = 2048
    addr = (host,port) 

    udpServer = socket(AF_INET,SOCK_DGRAM)
    udpServer.bind(addr) #开始监听

    while True:
        print('Waiting for connection...')
        data,addr = udpServer.recvfrom(bufsize)  #接收数据和返回地址
        print('Data Received')
        # save data locally
        saveLocal(data)
        # save data to database
        datetime_utc = datetime.now()
        wtPGDB(datetime_utc, data)
        saveAWSrds(datetime_utc, data)
    udpServer.close()

if __name__ == "__main__":
    main()