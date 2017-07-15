
import MySQLdb as mysql
import time
class DB:
    def __init__(self,host,user,passwd,db_name):
        self.conn = None
        self.cursor = None
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db_name
        self.connect()
    def connect(self):
        self.conn = mysql.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()
    def execute(self,sql):
        # error handle
        try: 
            self.cursor.execute(sql)    
            return self.cursor
        except mysql.OperationalError:
            # connect
            print 'reconnect db'
            self.connect()
            time.sleep(1)
            return self.execute(sql)
            
            # execute
    def list(self,table_name,col_name='*'):
        sql = 'select %s from %s'%(col_name,table_name)
        res = self.execute(sql)
        return res.fetchall() 
    def update(self):
        pass
    def delete(self):
        pass
    def add(self,table_name,add_dict):
        print add_dict
        if not ''.join(add_dict.values()):
            return {'code':1,'msg':'no data'}
        #'insert into xx  (name,mobile) values ("123","asd")'
        col_names = ','.join(add_dict.keys())
        values = ','.join(["'%s'"%v for v in add_dict.values()])
        sql = "insert into %s (%s) values (%s)"%(table_name,col_names,values)
        self.execute(sql)
        return {'code':0}
db = DB(host='59.110.12.72',user='woniu',passwd='123456',db_name='actual14')









