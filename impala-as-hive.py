# -*- coding: utf-8 -*-
from pyhive import hive

conn = hive.Connection(
    host='10.36.249.147',
    port=8703,
    username='',
    database='default',
    auth='NOSASL'
)

cursor = conn.cursor()
cursor.execute('select * from titanic')
for result in cursor.fetchall():
    print(result)
conn.close()
