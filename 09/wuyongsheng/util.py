# encoding:utf-8

import MySQLdb as mysql
import MySQLdb
import time


class DB:
    def __init__(self, host, port, user, pwd, database):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.database = database

    def connect(self):
        try:
            #con = mysql.connect(host='192.168.137.11', port=3376, user='root', passwd='123456', db='test',charset='utf8')
            self.conn = mysql.connect(host=self.host, port=self.port, user=self.user,
                                      passwd=self.pwd, db=self.database, charset='utf8')
            self.conn.autocommit(True)
            #cur = con.cursor()
        except Exception as e:
            print e
        # return cur

    def execute(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
        except Exception as e:
            print e
            try:
                # 关闭游标 数据库连接
                cur.close()
                self.conn.close()
            except:
                pass
            time.sleep(1)
            try:
                print 'reconnect DB!x1'
                # class中函数调用方法 self.functionName()
                # 再次连接数据库
                self.connect()
                cur = self.conn.cursor()
                cur.execute(sql)
            except Exception as e:
                print e
                # 若没有连接上 sleep 2秒，再次连接DB
                time.sleep(2)
                print 'reconnect DB!x2 '
                self.connect()
                cur = self.conn.cursor()
                cur.execute(sql)
        # 返回执行DB游标
        return cur

db = DB('192.168.137.11', 3376, 'root', '123456', 'test')


def select(sql):
    cur = db.execute(sql)
    data = cur.fetchall()
    return data
# sql = 'select * from user'
# print select(sql)


def chk_login(u, p, sql):
    # 登录验证
    cur = db.execute(sql)
    data = cur.fetchone()
    # print data[0],data[1]
    if cur.rowcount != 0:
        # 新增当用户或密码不存在时,做错误判断, 或跳转到新增页面=>错误提示
        if data[0] == u and data[1] == p:
            return 'ok'
        else:
            return 'wrong user %s or password' % (u)
    else:
        return 'user is %s or password is %s not exist' % (u, p)


def insert(u, p, sql):
    # 插入数据
    cur = db.execute(sql)
    return 'ok'


def del_user(u, sql):
    # 删除用户
    cur = db.execute(sql)
    if cur.rowcount == 1:
        return 'ok'
    else:
        return 'del %s not exists' % (u)


def chk_pwd(u, sql):
    # 旧密码验证
    cur = db.execute(sql)
    data = cur.fetchone()
    return data


def mod_pwd(newpwd, user, sql):
    # 修改密码
    cur = db.execute(sql)
    return 'ok'
