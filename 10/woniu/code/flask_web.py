
from flask import Flask,render_template,request,redirect,session
from dbutil import db
import json
app = Flask(__name__)




@app.route('/')
def index():
    return redirect('/idc')
@app.route('/idc')
def idc():
    return render_template('idc.html')
    #res = db.list('user')
    #return json.dumps(res)
@app.route('/user')
def user():
    return render_template('user.html')
@app.route('/pc')
def pc():
    return render_template('pc.html')


@app.route('/addapi',methods=['POST'])
def addapi():
    res_dict = request.form.to_dict()
    table_name = res_dict.pop('table_name')
    add_res = db.add(table_name,res_dict)
    return json.dumps(add_res)
    
@app.route('/listapi')
def listapi():
    table_name = request.args.get('table_name')
    res = db.list(table_name)
    return json.dumps(res)





if __name__=="__main__":
    app.run(host='0.0.0.0',port=9092,debug=True)












