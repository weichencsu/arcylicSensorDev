#!/usr/bin/env python3
import psycopg2
from datetime import datetime
# 获得连接
conn = psycopg2.connect(database="AcrylicSSDB_test", user="postgres", password="354877", host="127.0.0.1", port="5432")
# 获得游标对象
cursor = conn.cursor()
# get current time
datetime_utc = datetime.now()
print(datetime_utc)
# sql语句 建表
sql ="""INSERT INTO wearData (ts, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
params = (datetime_utc, 162, 0, 0, 32, 1, 10, 1, 0, 0, 78, 255, 255, 255, 254, 0, 0, 0, 4, 101, 42)
# 执行语句
cursor.execute(sql,params)
print("successfully")
# 事物提交
conn.commit()

# 关闭数据库连接
conn.close()
