from flask import Flask,request,render_template,session,redirect

app = Flask(__name__)
app.secret_key='8912jkxas809123ijhas980d213jihd9834husdf123980'


@app.route('/')
def hello_world():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user and pwd:
            if user == 'admin' and pwd == 'admin':
                session['user'] = 'admin'
                return redirect('/userlist')
            else:
                userinfo ={}
                with open('user.txt', 'r') as f:
                    content = f.readlines()
                for line in content:
                    userinfo[user], userinfo[pwd] = line.split(":")

                for user, pwd in userinfo.iteritems():
                    session['user'] = user
                    return redirect('/userlist')
                else:
                    return 'wrong username or password'
        else:
            return 'Please input the correct username and password'

@app.route('/logout')
def logout():
    del session['user']
    return redirect('/login')

@app.route('/userlist')
def userlist():
    userlist = []
    with open('user.txt') as f:
        for l in f:
            userlist.append(l.split(':'))
        return render_template('userlist.html', userlist=userlist, user=session.get('user'))


@app.route('/adduser', methods=['GET','POST'])
def adduser():
    if session.get('user') != 'admin':
        return 'you need login or not allowed user'
    if request.method == 'GET':
        return render_template('adduser.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        with open('user.txt', 'a') as f:
            f.write(user+':'+pwd+'\n')
        return redirect('/userlist')


@app.route('/deluser', methods=['GET', 'POST'])
def deluser():
    if session.get('user') != 'admin':
        return 'you need login or not have permission to del user'
    if request.method == 'GET':
        return render_template('deluser.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        with open('user.txt', 'r') as f:
            content = f.readlines()
            for line in content:
                    if line.startswith(user):
                        content.remove(line)
            with open('user.txt', 'w')as f:
                f.writelines(content)
                return redirect('/userlist')





if __name__ == '__main__':
    app.run(host='192.168.12.10', debug=True)
