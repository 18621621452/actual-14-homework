#!/bin/env python
# encoding:utf8
from flask import Flask,request,redirect,render_template,session
import util
import MySQLdb as mysql
app=Flask(__name__)
#生成密钥
app.secret_key="dsfdsf%$&^*1243GHkjkkkjhGFF5545657*(*@@*&&^%$$%asfddsf1242432544351HJHH55GGhhjjj$^%^43fds"
con = mysql.connect(host="localhost",user="root",passwd="Pass@123",db="python")
cur = con.cursor()
con.autocommit(True)
@app.route("/")
def index():
    if not session.get('user'):
        return redirect("/login")
    cur.execute("select * from user")
    return render_template("index.html",user_list=cur.fetchall(),user=session.get('user'))
#读取文件内容转为字典
#def users():
#    users={}
#    with open("user.txt") as f:
#       for l in f:
#            tmp=l.split(":")
#            u,p=tmp[0],tmp[1]
#            users[u]=p.strip("\n")
#    
#    return users
#登录页面,判断用户密码是否匹配并保存session
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method=="POST":
        user=request.form.get("user")
        pwd=request.form.get("pwd")
        sql = "select * from user where username='%s' and password='%s'"%(user,pwd)
        if  cur.execute(sql):
            session['user'] = user
            return redirect("/")
        else:
            return "wrong username or password"
#注销页面,删除session
@app.route("/logout")
def logout():
    del session['user']
    return redirect("/login")
#文件内容展示
#@app.route("/userlist",methods=["GET","POST"])
#def userlist():
#    user_list=[]
    #判断是否登录，未登录的跳转到登录页面
#    if not session.get("user"):
#        return redirect("/login")
#    with open("user.txt") as f:
#        for l in f:
#            user_list.append(l.split(":"))      
#    print session.get("user")
#    print user_list
#    return render_template("userlist.html",userxxx=user_list,user=session.get("user"))
#添加用户，用户名不允许重复
@app.route("/adduser",methods=["POST"])
def adduser():
 #   if request.method == "GET":
 #       return render_template("adduser.html")
#    elif request.method == "POST":
        user=request.form.get("user")
        pwd=request.form.get("pwd")
        if user and pwd:
            sql = "insert into user values ('%s','%s')"%(user,pwd)
            cur.execute(sql)
            return redirect("/")
        else:
            return "need username and password"
#删除用户
@app.route("/deluser",methods=["GET","POST"])
def deluser():
        user=request.args.get("user")
        serach_user = cur.execute("select * from user where username='%s'"%user)
        del_user = cur.execute("delete from user where username='%s'"%user)
        if serach_user:
            del_user
            print cur.fetchall()
            return redirect("/")
        else:
            return "username dose not exists"
@app.route("/update",methods=["GET","POST"])
def change_pwd():
    if request.method=="GET":
        user=request.args.get("user")
        return render_template("change_pwd.html",user=user)
    elif request.method=="POST":
        user=request.form.get("user")
        oldpwd=request.form.get("oldpass")
        newpwd=request.form.get("newpass")
        confirmpwd=request.form.get("confirmpass")
        print util.get_users
        sql = "select * from user where username='%s' and password='%s'"%(user,oldpwd)
        if not cur.execute(sql):
            return "wrong old password"
        if newpwd != confirmpwd:
            return "new password must equal to confirm password"
        sql = "update user set password='%s' where username='%s'"%(newpwd,user)
        update_pwd=cur.execute(sql)
        return redirect("/")
@app.route("/pc",methods=["GET","POST"])
def pc():
    mem=request.args.get("mem")
    sort_mem=request.args.get("sort_mem")
    sql="select * from pc"
    memorder=request.args.get("memorder")
    print memorder
    if memorder == 'up':
        sql +=' order by mem'
    elif memorder == 'down':
        sql +=' order by mem desc'
    print sql
    print sort_mem
    if sort_mem == 'zx':
          sql="select * from pc order by mem"
    elif sort_mem == 'dx':
          sql="select * from pc order by mem desc"
    cur.execute(sql)
    pc_list=cur.fetchall()
    mem_list=[]
    #获取内存列表
    for res in pc_list:
        m=res[2]
        if m not in mem_list:
            mem_list.append(m)
    new_pc=[]
    #获取PC列表
    for res in pc_list:
        if not mem or res[2]==int(mem):
            new_pc.append(res)
    return render_template("pc.html",pc=new_pc,res_list=mem_list)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=True)
