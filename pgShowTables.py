#!/usr/bin/env python3
import psycopg2

# Start a PostgreSQL database session

conn = psycopg2.connect(database="AcrylicSSDB_test", user="postgres", password="354877", host="127.0.0.1", port="5432")
# 获得游标对象
cursor = conn.cursor()

cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
for table in cursor.fetchall():
    print(table)


# Free the resources
cursor.close()
conn.close()

