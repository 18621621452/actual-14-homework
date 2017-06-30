import MySQLdb as mysql

user_dict = {}
# # from txt to dict
# def get_data_from_file():
#     with open('user.txt') as f:
#         for l in f:
#             if l=='\n':
#                 continue
#             (user,pwd) = l.replace('\n','').split(':')
#             user_dict[user] = pwd
#     print user_dict
# get_data_from_file()
#
# #from dict to txt
# def render_file_from_dict():
#     user_txt_list = []
#     print user_dict
#     for item in user_dict.items():
#         user_txt_list.append('%s:%s'%item)
#     print user_txt_list
#     with open('user.txt','w') as f:
#         f.write('\n'.join(user_txt_list))
#
#
# def add_user(user,pwd):
#     if user and pwd:
#         if user in user_dict:
#             return 'user already exist'
#         else:
#             user_dict[user] = pwd
#             render_file_from_dict()
#             return 'ok'
#     else:
#         return 'need a user and password'
#
# def del_user(user):
#     if not user:
#         return 'need a username'
#     if user in user_dict:
#         del user_dict[user]
#         render_file_from_dict()
#         return 'ok'
#     else:
#         return 'user not exists'
#
# def updateuser(user,pwd):
#     user_dict[user] = pwd
#     render_file_from_dict()
#
# def login(user,pwd):
#     pass


con = mysql.connect(host='192.168.12.10', user='gamedb', passwd='gamepass@gs.jibei.com', db='actual14')
con.autocommit(True)
cur = con.cursor()


def read_from_mysql():
    cur.execute("select * from user")
    user_dict = cur.fetchall()
    return user_dict


def write_to_mysql(user, pwd):
    cur.execute("INSERT INTO user VALUES ('{0}','{1}');".format(user, pwd))
    cur.fetchall


def update_mysql(user, pwd):
    cur.execute("UPDATE  user SET passwd='{pwd}' WHERE username='{user}';".format(user=user,pwd=pwd))
    return cur.fetchone


def delete_mysql(user):
    cur.execute("DELETE FROM user WHERE username='{0}';".format(user))
    cur.fetchall

def where_mysql(user, pwd):
    cur.execute("select * from user WHERE username ='{0}' AND passwd='{1}'".format(user, pwd))
    return cur.fetchone


def exists_user(user):
    res = cur.execute("select '{0}' from user WHERE username='{0}';".format(user))
    return res


def pc_asc():
    cur.execute("select * from pc ORDER BY 'mem';")
    result = cur.fetchall()
    return result


def pc_desc():
    cur.execute("select * from pc ORDER BY 'mem' DESC ;")
    result = cur.fetchall()
    return result