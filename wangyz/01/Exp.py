#encoding:utf-8

# 列表
lstA=list('hello')
# for item in lstA:
# 	print item

# len 函数
print '列表的长度len():',len(lstA)

print "count():",lstA.count('h'),lstA.count('w')

lstA.insert(2,'$')
print "lstA:",lstA

print "-------------------append"
lstA.append("^")
print lstA


print "-------------------extend"
lstb=['A','C','B','D']
lstA.extend(lstb)
print lstA

print "-------------------remove"
lstA.remove('o')
print lstA

print "-------------------pop"
lstA.pop()
print lstA

