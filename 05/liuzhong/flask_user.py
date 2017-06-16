#!/bin/env python
# encoding:utf8
from flask import Flask,request,redirect,render_template,session
app=Flask(__name__)
#生产密钥
app.secret_key="dsfdsf%$&^*1243GHkjkkkjhGFF5545657*(*@@*&&^%$$%asfddsf1242432544351HJHH55GGhhjjj$^%^43fds"
#读取文件内容转为字典
def users():
    users={}
    with open("user.txt") as f:
       for l in f:
            tmp=l.split(":")
            u,p=tmp[0],tmp[1]
            users[u]=p.strip("\n")
    return users
#登录页面,判断用户密码是否匹配并保存session
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method=="POST":
        user=request.form.get("user")
        pwd=request.form.get("pwd")
        if user and pwd:
            if user in users().keys():
                if pwd == users()[user]:
                    session['user'] = user
                    return redirect('/userlist')
                else:
                    return "wrong username or password"
            else:
                return "username dose not exists" 
        else:
            return "you need login"
#注销页面,删除session
@app.route("/logout")
def logout():
    del session['user']
    return redirect("/userlist")
#文件内容展示
@app.route("/userlist",methods=["GET","POST"])
def userlist():
    user_list=[]
    #判断是否登录，未登录的跳转到登录页面
    if not session.get("user"):
        return redirect("/login")
    with open("user.txt") as f:
        for l in f:
            user_list.append(l.split(":"))      
    print session.get("user")
    print user_list
    return render_template("userlist.html",userxxx=user_list,user=session.get("user"))
#添加用户，用户名不允许重复
@app.route("/adduser",methods=["GET","POST"])
def adduser():
    if request.method == "GET":
        return render_template("adduser.html")
    elif request.method == "POST":
        user=request.form.get("user")
        pwd=request.form.get("pwd")
        with open("user.txt","a") as f:
            if user and pwd:
                if user in users().keys():
                    return "username has exists,please try again!"
                else:
                    f.write(user+":"+pwd+"\n")
                    print user,pwd
                    return redirect("/userlist")
            else:
                return "username and password canont be empty"
#删除用户
@app.route("/deluser",methods=["GET","POST"])
def deluser():
    if request.method=="GET":
        return render_template("deluser.html")
    elif request.method=="POST":
        user=request.form.get("user")
        print user,users().keys()
        #不能修改其他函数里的值，需要赋值到新的变量
        if user in users().keys():
            users_new=users()
            users_new.pop(user)
            print users_new
        else:
            return "username dose not exists"
        #清空文件内容
        with open("user.txt","w") as f:
            f.truncate()
       #写入新的内容
        with open("user.txt","a") as f:
            for user,pwd in users_new.items():
                print user,pwd
                f.write(user+":"+pwd+"\n")
        return redirect("/userlist")
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8081,debug=True)
