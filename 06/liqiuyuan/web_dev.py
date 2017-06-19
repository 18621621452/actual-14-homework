
from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
import util
import os

# use random
app.secret_key = os.urandom(24)



@app.route('/')
def index():
    if 'user' in session:
        return render_template('index.html',user=session['user'], users=util.read_from_mysql())
    else:
        return redirect('/login')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if util.where_mysql(user, pwd):
            session['user'] = user
            return redirect('/')
        else:
            return 'wrong user or password'

@app.route('/adduser', methods=['GET','POST'])
def adduser():
    if session.get('user') != 'admin':
        return 'you need login or not allowed user'
    if request.method == 'GET':
        return render_template('adduser.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        res = util.exists_user(user)
        if res:
            return 'user exists'
        else:
            util.write_to_mysql(user, pwd)
            return redirect('/')



@app.route('/updatepwd',methods=['GET','POST'])
def updatepwd():
    if request.method=='GET':
        user = request.args.get('user')
        return render_template('update.html', user=user)
    elif request.method=='POST':
        user = request.form.get('user')
        oldpwd = request.form.get('oldpwd')
        newpwd = request.form.get('newpwd')
        confirmpwd = request.form.get('confirmpwd')
        if util.where_mysql(user,oldpwd):
            if newpwd != confirmpwd:
                return 'new pwd not equal to confirmpwd'
            else:
                util.update_mysql(user, newpwd)
                return redirect('/')
        else:
            return "wrong old passwd"

@app.route('/delete')
def removeuser():
    user = request.args.get('user')
    util.delete_mysql(user)
    return redirect('/')


@app.route('/logout')
def logout():
    del session['user']
    return redirect('/login')


if __name__ == "__main__":
    app.run(host='192.168.12.10', debug=True)










