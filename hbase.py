# coding=utf-8

import happybase
conn = happybase.Connection("gzbh-intel016.gzbh", 8720)

print(conn.tables())
# xxx 表示表名，在连接之前要先在终端创建表
table = conn.table("user")
print(table.scan())

for k, v in table.scan():
    print(k, v)