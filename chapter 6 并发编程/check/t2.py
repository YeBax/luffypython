# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    password='123456',
    database='student',
    charset='utf8',
)


cur = conn.cursor()
sql = '''insert into student1(sname, gender, credit)  VALUES (%s,%s,%s)'''
cur.execute(sql, ("bax",'男','001'))
conn.commit()
cur.close()
conn.close()


