#encoding:utf-8
'''
作业：
   ajax 修改密码
'''
import util
from flask import Flask, session, request, render_template, redirect
app = Flask(__name__)
# 引入cookie 安全认证
app.secret_key = 'rtyuiopghjk67894356789fgbhjnmk3456t7yu8ioghjk'

#@app.route('/ajax')
#def ajax():
#    return render_template('ajax.html')

#@app.route('/ajaxlist')
#def ajaxlist():
#    tmplist = []
#    with open('t.txt') as f:
#        for l in f:
#            tmplist.append(l.split(':'))
#    return render_template('ajaxlist.html', users=tmplist)


@app.route('/userlist')
def userlist():
    # 用于ajax 数据异步显示
    sql = 'select * from user'
    res = util.select(sql)
    print res
    return render_template('userlist.html',users = res)

@app.route('/index')
def index():
    sql = 'select * from user'
    res = util.select(sql)
    print res
    if not session['user']:
        return redirect('/login') 
    else:
        return render_template('index.html', user = session.get('user'), users = res)

@app.route('/login', methods=['GET','POST'])
def login():
    # 登录页面
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd  = request.form.get('pwd')
        print '*'*20
        print user,pwd
        print '*'*20
        if user and pwd:
            # 验证登录用户
            sql = 'select * from user where username="%s"'%(user)
            res = util.chk_login(user,pwd,sql)
            if res == 'ok': 
                session['user'] = user
                return redirect('/index')
            else:
                return res
  
@app.route('/adduser')
def adduser():
    # 新增用户
    user = request.args.get('user') 
    pwd  = request.args.get('pwd')
    sql = 'insert into user values("%s","%s");'%(user,pwd)
    res = util.insert(user,pwd,sql)
    if res == 'ok':
        return redirect('/index')    
    else:
        return res

@app.route('/deluser')
def removeuser():
    # 删除数据
    user = request.args.get('user')
    sql = 'delete from user where username = "%s"'%(user)
    res = util.del_user(user, sql)
    if res == 'ok':
        return redirect('/index')
    else:
        return res

@app.route('/update',methods=['GET','POST'])
def updatepwd():
    # 修改用户密码
    if request.method == 'GET':
        # 将更新用户名 传入前端
        user = request.args.get('user')
        return render_template('updatepwd.html', user = user)
    elif request.method == 'POST':
        user = request.form.get('user')
        oldpwd = request.form.get('oldpwd')
        newpwd = request.form.get('newpwd')
        confirmpwd = request.form.get('confirmpwd')
        sql = 'select password from user where username = "%s"'%(user)
        print sql
        cur = util.connect()
        cur.execute(sql)
        data = cur.fetchone()
        print data[0]
        if oldpwd == data[0] and (newpwd == confirmpwd):
            sql = 'update user set password = "%s" where username = "%s"'%(newpwd,user)
            cur.execute(sql)
            return redirect('/index')
        else:
            return 'olpwd or newpwd not eque confirmpwd'
         
@app.route('/logout')
def logout():
    # 退出时 从cookie中清除登录的用户
    del session['user']
    return redirect('/login')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9081, debug=True)
