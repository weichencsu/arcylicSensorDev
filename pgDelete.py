#!/usr/bin/env python3
import psycopg2

# Start a PostgreSQL database session

conn = psycopg2.connect(database="AcrylicSSDB_test", user="postgres", password="354877", host="127.0.0.1", port="5432")
# 获得游标对象
cursor = conn.cursor()

tableName = "wearData"

# Form the SQL statement - DROP TABLE
dropTableStmt = "DROP TABLE %s;"%tableName
# Execute the drop table command
cursor.execute(dropTableStmt)
# Free the resources
conn.commit()
# 关闭数据库连接
conn.close()
