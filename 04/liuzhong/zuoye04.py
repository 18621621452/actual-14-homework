#!/bin/env python
# encoding:utf8
#从日志中读取内容并转为字典
def read_log(file):
    with open(file) as f:
    	res={}
        for l in f:
            if l == '\n':
                continue
            tmp = l.split()
            ip,url,status = tmp[0],tmp[6],tmp[8]
            res[(ip,url,status)] = res.get((ip,url,status),0)+1
    return res
#以ip,url,status三个维度按数量排序取前十名可并列 ，并写入html文件
def paixu(log):
    res_list = read_log(log).items()
    length = len(res_list)
    for j in range(length-1):
        for i in range(length-1-j):
            if res_list[i][1] > res_list[i+1][1]:
                res_list[i],res_list[i+1] = res_list[i+1],res_list[i]
        if j >=10:
            if res_list[-j][1] != res_list[-j-1][1]:
                sort_length = j
                break
    with open('index.html','w') as f:
    	text = "<table border='1'><tr><td>ip</td><td>url</td><td>status</td><td>count</td></tr>"
    	for (ip,url,status),count in res_list[:-sort_length-1:-1]:
    		text +="<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"%(ip,url,status,count)
    	text +='</table>'
        f.write(text)
    return 'ok'
print paixu('/root/log.log')
