from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)

#use random
app.secret_key='skc2iu4y1289mjf67891xncghfk830x230c88dkcuf63'

@app.route('/login',methods=['GET','POST'])
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
                return 'wrong user or password,please input again'
        else:
            return 'need username and password'

@app.route('/logout',methods=['GET','POST'])
def logout():
    del session['user']
    return redirect('/userlist')

@app.route('/')
def index():
    return 'hello flask!!!'

@app.route('/userlist')
def userlist():
    userlist = []
    with open('user.txt') as f:
        for l in f:
            userlist.append(l.split(':'))
        return render_template('userlist.html',userxxx=userlist,user=session.get('user'))

@app.route('/user')
def user():
    html_str = '<table border="1">'
    with open('user.txt') as f:
        for line in f:
            html_str += '<tr><td>%s</td><td>%s</td></tr>'%tuple(line.split(':'))
    return html_str


@app.route('/adduser',methods=['GET','POST'])
def adduser():
    if session.get('user') != 'admin':
        return 'you need login or not allowed user'
    if request.method == 'GET':
        return render_template('adduser.html')
    elif request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        with open('user.txt','a') as f:
            print user,'|'*30,pwd
            f.write(user+':'+pwd+'\n')
        return redirect('/userlist')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8999,debug=True)
