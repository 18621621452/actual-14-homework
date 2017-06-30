#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
@file: autoopenserver.py
@time: 2017/6/26 9:24
"""
import json
import urllib2
import MySQLdb

# 登录服务器IP或者域名
ls_ip = 'htls.jibeigames.com'

def get_last_sid(ls_ip):
    req = urllib2.urlopen('http://{0}/serverlist/server_cfg.json'.format(ls_ip))
    response = req.read()
    responseJSON = json.loads(response)

    sid = []
    for i in responseJSON['server_list']:
        sid.append(i['id'])
    return sid[-1]

def get_users():
    con = MySQLdb.connect(host='',user='gamedb', passwd='',db='')
    cursor = con.cursor()
    cursor.execute('select count(*) from htlive.user where sid=1;')
    print cursor.fetchall()

