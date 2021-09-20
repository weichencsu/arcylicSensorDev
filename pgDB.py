#!/usr/bin/env python3
import psycopg2
# 获得连接
conn = psycopg2.connect(database="AcrylicSSDB_test", user="postgres", password="354877", host="127.0.0.1", port="5432")
# 获得游标对象
cursor = conn.cursor()
# sql语句 建表
sql = """CREATE TABLE wearData (
ts TIMESTAMPTZ,
b1 int4,
b2 int4,
b3 int4,
b4 int4,
b5 int4,
b6 int4,
b7 int4,
b8 int4,
b9 int4,
b10 int4,
b11 int4,
b12 int4,
b13 int4,
b14 int4,
b15 int4,
b16 int4,
b17 int4,
b18 int4,
b19 int4,
b20 int4);"""
# 打印
cursor.execute(sql)
print("wearData table created successfully")
# 事物提交
conn.commit()
# 关闭数据库连接
conn.close()

