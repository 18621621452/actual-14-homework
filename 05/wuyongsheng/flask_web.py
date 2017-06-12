#encoding:utf-8
"""
作业：
    用户名密码，存储文件
    支持用户登陆，分为普通用户和管理员用户（通过用户名来区分即可）
            管理员账号写死 admin admin


    1.如果是普通用户，能看到列表，但是不能操作
    2.如果是管理员，可以对用户进行体添加，删除 ，新添加的用户，也可以登陆
    3.没有登陆的，列表页会跳转到login
    4.支持logout
    5 用户名密码存储格式 用户1:密码\n
"""
# 引入相应模块
from flask import Flask,render_template,redirect,session,request
# Flask 实例化对象app
app = Flask(__name__)
# 设置cokie中session安全认证
app.secret_key='fghjklcvbnmtyuio2345678dfghjpldqazk'

def file2dict():
    # 将文件user.txt 转换成字典
    result = {}
    with open('user.txt','r') as f:
        for line in f:
            line = line.strip().split(':')
            if line[0] == 'user' and line[1] == 'pwd':
                # 跳过首行
                continue
            result.setdefault(line[0],line[1])
    return result

def chk_user(u,p):
    # 校验user/pwd
    user = file2dict()
    if user.get(u,None) != p:
            return True

def user_unique(u):
    # 校验user唯一性
    user = file2dict() 
    if u in user.keys():
        return True

def del_user(u,isdel=False):
    # 删除普通用户
    user = file2dict()
    if u in user.keys():
        del user[u]
        isdel = True
    with open('user.txt','w') as f:
        f.write('user'+':'+'pwd'+'\n')
        for k,v in user.items():
            f.write(k+':'+v+'\n')
    return isdel 

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        # GET显示html页面
        return render_template('login.html')
    elif request.method == 'POST':
        # POST向html页面中form提交数据
        user = request.form.get('username')
        pwd = request.form.get('password')
        #校验user.txt中user:pwd是否已经存在
        if chk_user(user,pwd):
            return 'user/pwd not exists,please add user'
        if user and pwd:
            # 将登陆的用户加入session
            session['user'] = request.form.get('username')
            if user == 'admin' and pwd == 'admin':
                #session['user'] = 'admin' 
                # admin 用户可添加、删除用户 如这里admin加session中 对普通用户不跳转页面,故在if之前加
                return redirect('/userlist') 
            else:
                #print 'normal user is %s/%s'%(user,pwd)
                # 普通用户查询userlist
                return redirect('/userlist')
        else:
            return 'need user and pwd or not allowed login'

@app.route('/logout')
def logout():
    # 清空cookie中的值 
    #del session['user'] 
    session.pop('user',None)
    return redirect('/login')

@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    # 新增加用户
    if session.get('user') != 'admin':
        # 只有admin才能新增用户 否则是普通用户 将被拒
        return 'add user and need admin logined' 
    if request.method == 'GET':
        return render_template('adduser.html')
    elif request.method == 'POST':
        user = request.form.get('username')
        pwd  = request.form.get('password')
        if user_unique(user):
            # 写入user.txt中 判断user是否在文件中已存在
            return 'user %s has existed'%(user) 
        with open('user.txt','a') as f:
            f.write(user+':'+pwd+'\n')
        return redirect('/userlist') 

@app.route('/userlist')
def userlist():
    # userlist 页面显示
    if session.get('user') is None:
        # 如没有登录 列表页直接跳到login
        return redirect('/login') 
    userlist = []
    with open('user.txt','r') as f:
        for line in f:
            userlist.append(line.split(':'))
    return render_template('userlist.html', userlist = userlist, user=session.get('user')) #这里user取 session中值 用于判断普通或管理用户

@app.route('/deluser', methods=['GET','POST'])
def deluser():
    # 删除普通用户
    if session.get('user') != 'admin':
        return 'del user and need admin user logined'
    if request.method == 'GET':
        return render_template('deluser.html')
    elif request.method == 'POST':
        user = request.form.get('username')
        if user == 'admin':
            return '管理员admin 不能删除'
        elif del_user(user):
            return redirect('/userlist')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9081, debug=True)
