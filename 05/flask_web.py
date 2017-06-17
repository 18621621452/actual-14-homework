from flask import Flask,render_template,request,redirect,session
import time
import subprocess


app = Flask(__name__)
app.secret_key='abcdefghigklmnopgistuvwxyz'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('pwd')
        if user and pwd:
            if user == 'admin' and pwd == 'admin':
                session['user'] = 'admin'
                return redirect('/userlist')
            else:
                with open('a.txt','r') as foo:
                    for line in foo.readlines():
                        if user == line.split(':')[0] and pwd == line.split(':')[1].strip(): 
                            session['user'] = user
                            return redirect('/nomaluserlist')
                    return '----------------------- not correct!!!' 
                          
        else:
            return 'you need input your username or passwd!!!!!!!!!!!!!!'

@app.route('/logout')
def logout():
    del session['user']
    return redirect('/login')

@app.route('/userlist')
def userlist():
    print session.get('user')
    if session.get('user') == None:
        return 'please login first!!'
    
    userlist = []
    with open('a.txt') as f:
        for line in f:
            userlist.append(line.split(':'))
        return render_template('userlist.html',userxxx=userlist,user=session.get('user'))

@app.route('/nomaluserlist')
def nomaluserlist():
    print session.get('user')
    if session.get('user') == None:
        return 'please login first!!'
    else:
        userlist = []
        with open('a.txt') as f:
            for line in f:
                userlist.append(line.split(':'))
            return render_template('nomaluserlist.html',userxxx=userlist,user=session.get('user'))

@app.route('/adduser',methods = ['GET','POST'])
def adduser():
    print session.get('user')
    print '*'*50
    #if session.get('user') != 'admin':
    #    return 'you need login or not allowed this user'
    if request.method == 'GET':
        return render_template('adduser.html')
    elif request.method =='POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        with open('a.txt','a') as f:
            f.write(user+':'+pwd+'\n')
    return redirect('/userlist')

@app.route('/deleteuser/',methods=['GET','POST'])
def deleteuser():
    user = request.args.get('user', '')
    print user
    print '*'*50
    with open("a.txt","r") as f:
        lines = f.readlines()
        #print(lines)
    with open("a.txt","w") as f_w:
        for line in lines:
            if user in line:
                continue
            f_w.write(line)
    return redirect('/userlist')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7799,debug=True)
















