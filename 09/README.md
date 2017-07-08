

# 完善第八次作业
# 操作数据库封装类，重启数据库后可以重连

```

dbutil
class DB:

    __init__(self,host,user,pwd,database):
        connentxxx
    excute()
        try:
            执行sql
        except Exception as e:
            如果报错，重新连接数据库，再执行sql
    fetchall()


db = DB()

db.excute(sql)


```