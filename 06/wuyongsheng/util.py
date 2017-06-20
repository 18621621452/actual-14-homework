#encoding:utf-8

import MySQLdb as mysql

def connect():
    try:
        con = mysql.connect(host='192.168.137.01', port=x376, user='root', passwd='123456', db='test',charset='utf8')
        con.autocommit(True)
        cur = con.cursor()
    except Exception as e:
        print e
    return cur

def select(sql):
    cur = connect()
    cur.execute(sql)
    data = cur.fetchall()
    return data

def chk_login(u, p, sql):
    # 登录验证
    cur = connect()
    cur.execute(sql)
    data = cur.fetchone()
    #print data[0],data[1]
    if data[0] == u and data[1] == p:
        return 'ok'
    else:
        return 'wrong user %s or password'%(u)

def insert(u, p, sql):
    # 插入数据
    cur = connect()
    # 去重
    sql_un = 'select username from user where username = "%s"'%(u)
    print sql_un
    cur.execute(sql_un)
    if not cur.fetchone():
        cur.execute(sql)
        return 'ok'
    else:
        return 'user %s already exist'%(u)

def del_user(u, sql):
    # 删除用户
    cur = connect()
    cur.execute(sql)
    if cur.rowcount == 1:
        return 'ok'
    else:
        return 'del %s not exists'%(u)

#user = 'reboot'
#pwd = 'admin'
#sql = 'delete from user where username = "%s"'%(user)
#sql = 'select * from user where username="%s"'%(user)
#sql = 'insert into user values("%s","%s");'%(user,pwd)
#print insert(user,pwd ,sql)
#del_user(user, sql)    
