# encoding: utf-8
from flask import Flask, render_template, request, redirect, session
import MySQLdb as mysql

con = mysql.connect(host='localhost', user='root', passwd='123456', db='actual14')
con.autocommit(True)
cur = con.cursor()

app = Flask(__name__)
app.secret_key = '87983928730940809746262'


@app.route('/')
def index():
    return redirect('/login')


@app.route('/pc')
def pc():
    mem = request.args.get('mem')
    sql = 'select * from pc'
    print mem
    cur.execute(sql)
    res = cur.fetchall()
    mem_list = []
    for item in res:
        m = item[1]
        if m not in mem_list:
            mem_list.append(m)
    pc_list = []
    for item in res:
        print item, [mem]
        if not mem or (item[1] == int(mem)):
            pc_list.append(item)
    print pc_list
    return render_template('pc.html', pc=pc_list, mem_list=sorted(mem_list))


@app.route('/userlist')
def userlist():
    cur.execute('select * from user')
    return render_template('index.html', info=cur.fetchall(), user=session.get('user'))
    return 'ok'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login_bootstrap.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        sql = 'select * from user where username="%s" and password="%s"' % (user, pwd)
        print sql
        cur.execute(sql)
        if cur.fetchone():
            print cur.fetchone()
            session['user'] = user
            return redirect('/userlist')
        else:
            return 'wrong user or password'


@app.route('/logout')
def logout():
    return redirect('/')


@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if request.method == 'GET':
        return render_template('adduser.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        sql = "select * from user where username = '%s'" % user
        print sql, cur.execute(sql)
        if cur.execute(sql) != 0:
            return 'user exitsts'
        if user and pwd:
            sql = "insert into user values ('%s','%s')" % (user, pwd)
            cur.execute(sql)
            return redirect('/userlist')
        else:
            return 'input user and pwd'


@app.route('/deluser')
def deluser():
    user = request.args.get('user')
    print user
    if user and user != 'admin':
        sql = "delete from user where username = '%s'" % user
        print sql
        cur.execute(sql)
        return redirect('/userlist')
    else:
        return 'can not del admin'


@app.route('/changepwd', methods=['GET', 'POST'])
def changepwd():
    if request.method == 'GET':
        user = request.args.get('user')
        return render_template('changepwd.html', user=user)
    elif request.method == 'POST':
        user = request.form.get('user')
        oldpwd = request.form.get('oldpwd')
        newpwd = request.form.get('newpwd')
        verify_newpwd = request.form.get('verify_newpwd')
        print user, oldpwd, newpwd, verify_newpwd
        pwd = "select username from user where password = '%s'" % oldpwd
        print pwd, cur.execute(pwd)
        if cur.execute(pwd) == 1:
            if newpwd == verify_newpwd:
                update_pwd = "update user set password ='%s' where username = '%s'" % (newpwd, user)
                print update_pwd
                cur.execute(update_pwd)
                return redirect('userlist')
            else:
                return 'newpwd verify error'
        else:
            return 'old password not ture'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8800, debug=True)
