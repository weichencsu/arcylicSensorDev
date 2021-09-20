import psycopg2
# 获得连接
conn = psycopg2.connect(database="AcrylicSSDB_test", user="postgres", password="354877", host="127.0.0.1", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()
# sql语句 建表
sql ="""SELECT * FROM wearData;"""
# 执行语句
cursor.execute(sql)
# 抓取
rows = cursor.fetchall()
print(rows)
# 事物提交
conn.commit()
# 关闭数据库连接
cursor.close()
conn.close()
