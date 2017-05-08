#!/usr/bin/env python
#coding:utf8
#求出list表中，每个字符出现的次数
li = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']
res = {}
for m in li:
    if m in res:
        res[m]=res[m]+1
    else:
        res[m]=1
print res
