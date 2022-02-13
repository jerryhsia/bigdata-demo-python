# -*- coding: utf-8 -*-
from pyhive import hive

conn = hive.Connection(
     host='gzbh-intel016.gzbh',
     port=8719,
     username='root',
     database='default')

cursor = conn.cursor()
cursor.execute('show tables')
for result in cursor.fetchall():
    print(result)
conn.close()
