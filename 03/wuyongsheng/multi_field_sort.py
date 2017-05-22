#encoding:utf-8
# 按照多维度ip url status 数据统计

import pprint
count = {}

# 打开文件
f = open('www.log','r')

# 遍历文件及统计数据
for row in f:
    arr = row.split()
    #print arr
    ip = arr[0]
    url = arr[6]
    status = arr[8]
    count[(ip,url,status)] = count.get((ip,url,status),0)+1

# 关闭文件
f.close()

#print pprint.pprint(count)

# 字典转换成列表
arr = count.items()

# 冒泡10次
for i in range(10):
    for j in range(len(arr)-1-i):
        if arr[j][1] > arr[j+1][1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

# 取列表中top10
for k,v in arr[:-11:-1]:
    ip, url, status = k
    print "ip:%s url:%s status %s count:%s"%(ip,url,status,v)

