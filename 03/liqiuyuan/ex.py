#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
@file: ex.py
@time: 2017/5/20 17:47
"""

with open('www_access_20140823.log', 'r') as f:
    content = f.readlines()

# 生成{(ip,statu,url):10}的字典
new_dict = {}
for line in content:
    line = line.split(' ')

    ip = line[0]
    statu = line[8]
    url = line[10]

    res = tuple([ip, statu, url])

    if res in new_dict:
        new_dict[res] += 1
    else:
        new_dict[res] = 1

# 字典按照value排序
res = new_dict.items()
for j in xrange(len(res)):
    for i in xrange(len(res) - j - 1):
        if res[i][1] < res[i+1][1]:
            res[i], res[i+1] = res[i+1], res[i]


for k, v in res[:10:]:
    ip, statu, url = k
    print 'ip:{0},status:{1},url:{2},count:{3}'.format(ip, statu, url, v)

