#!/usr/bin/env python
#-*- coding:utf-8 -*-

File = open('/Users/playcrab/python/test/www_access_20140823.log','r')

Dict = {}
Tuple = ()
List = []

for line in File.readlines():
    num = 0
    ip = line.split()[0]
    url = line.split()[10].split('"')[1]
    status = line.split()[8]
    Tuple = (ip,url,status)
    Dict[Tuple] = Dict.get(Tuple,0) +1

#字典转成列表
List = Dict.items()

#排序
Length = len(List)
for k in range(Length-1):
    for j in range(Length-k-1):
        if List[j][1] < List[j+1][1]:
            List[j],List[j+1]=List[j+1],List[j]

for i in range(Length-1):
    if List[i][1] != List[i+1][1]:
        num += 1
    if num == 10:
        index = i
        break

num = 0
for k,v in List[0:index+1]:
    num = num + 1
    print "(%s) ip:%s||url:%s||status:%s||count:%s" %(num,k[0],k[1],k[2],v)

