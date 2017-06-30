#encoding:utf-8
from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = '87983928730940809746262'

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    print request.method
    if request.method == 'GET':
        return render_template('login_bootstrap.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        print 'user:%s pwd:%s' %(user,pwd)
        if user and pwd:
            if user == 'admin' and pwd == 'admin':
                session['user'] = 'admin'
                return redirect('/userlist')
            else:
                with open('user_pwd.txt', 'r') as f:
                    for line in f:
                        find_user = line.find(user)
                        if find_user == 0:
                            file_pwd = line.split(":")[1].split('\n')[0]
                            if file_pwd != pwd:
                                print 'file_pwd:%s,pwd:%s' % (file_pwd,pwd)
                                return '密码错误请重新输入'
                            else:
                                session['user'] = user
                                return redirect('/userlist')
                    return '没有此用户'
        else:
            return '请输入用户名和密码'

@app.route('/logout')
def logout():
    del session['user']
    return redirect('/login')

@app.route('/adduser',methods=['GET','POST'])
def adduser():
    print session.get('user')
    print '*'*40
    if session.get('user') != 'admin':
        return '非管理员账户无法添加'
    if request.method == 'GET':
        return render_template('adduser.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
    with open('user_pwd.txt', 'a') as f:
        print user,'|'*20,pwd
        if user:
            f.write(user + ':' + pwd + '\n')
    return redirect('/userlist')

@app.route('/deluser',methods=['GET','POST'])
def deluser():
    print session.get('user')
    print '*'*40
    if session.get('user') != 'admin':
        return '非管理员账户无法删除'
    if request.method == 'GET':
        return render_template('deluser.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        print 'delete user:%s' % user
    with open('user_pwd.txt', 'r') as f:
        lines = f.readlines()
    with open('user_pwd.txt', 'w') as f_w:
        for line in lines:
            if user  and user in line:
                continue
            f_w.write(line)
    return redirect('/userlist')

@app.route('/userlist')
def userlist():
    userlist = []
    with open('user_pwd.txt') as f:
        for line in f:
            userlist.append(line.split(':'))
    return render_template('userlist.html',userinfo=userlist,user=session.get('user'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)

