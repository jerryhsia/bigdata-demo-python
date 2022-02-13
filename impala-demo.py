from impala.dbapi import connect

conn = connect(
    host='10.36.249.147',
    port=8703)

cursor = conn.cursor()
cursor.execute('select * from titanic')
for result in cursor.fetchall():
    print(result)
conn.close()