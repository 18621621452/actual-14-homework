#encoding:utf-8

import MySQLdb as mysql

def connect():
    try:
        con = mysql.connect(host='192.168.137.11', port=3376, user='root', passwd='123456', db='test',charset='utf8')
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
    if cur.rowcount != 0:
        # 新增当用户或密码不存在时,做错误判断, 或跳转到新增页面=>错误提示
        if data[0] == u and data[1] == p:
            return 'ok'
        else:
            return 'wrong user %s or password'%(u)
    else:
        return 'user is %s or password is %s not exist' %(u,p)
#user = 'adm'
#pwd = 'adm'
#sql = 'select * from user where username = "%s"' %user
#print chk_login(user,pwd,sql)

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
