#coding=utf-8
#处理日志，按照访问者的IP和url和状态码三个维度统计数据，打印出现次数最多的10个
#定义一个count_dict key为（ip,url,status）value为数量
#遍历文件统计key数量
#排序
count_dict = {}
file_tuple = ()
all_list = []
#读取文件内容切割相应变量
with open('www_access_20140823.log', 'r') as f:
    for line in f.readlines():
        num = 0
        ip = line.split()[0]
        url = line.split()[10].split('"')[1]
        status = line.split()[8]
        file_tuple = (ip,url,status)
        count_dict[file_tuple] = count_dict.get(file_tuple,0) + 1
#dict转成list
all_list = count_dict.items()
#排序
length  = len(all_list)
for i in range(length-1):
    for j in range(length-i-1):
        if all_list[j][1] < all_list[j+1][1]:
            all_list[j],all_list[j+1]=all_list[j+1],all_list[j]
#判断并列数量
for i in range(length-1):
    if all_list[i][1] != all_list[i+1][1]:
        num += 1
    if num == 10:
        index = i
        break
#打印前十
num = 0
for key,value in all_list[0:index+1]:
    num += 1
    print "(%s) ip:%s||url:%s||status:%s||count:%s" %(num,key[0],key[1],key[2],value)

