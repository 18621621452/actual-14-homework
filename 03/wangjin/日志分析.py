#!/usr/bin/python
#coding:utf8


with open('access.mad') as f:
    content = f.readlines()
    f.close()

count_dict = {}

for line in content:
    line = line.split(' ')     #string 通过split 转换为list
    local_ip,uri,code = line[0],line[6],line[8]

    count_dict[(local_ip,uri,code)] = count_dict.get((local_ip,uri,code),0) + 1      #利用元组来作为key，然后统计数量

count_dict = sorted(count_dict.items() ,key=lambda item:item[1],reverse=True)        #这个排序的功能网上copy的，不了解原理

#下面进行重复行计数为一行。
n = 1                              #取行计数
num = 0                            #用于判断'统计数量'是否出现一样的
print ('---IP--------------URI----------CODE------count---')
for i in count_dict:
    if n <= 10:                    #取前十
        if i[1] != num:
            print ('%-10s%20s%5s%10s   ---->no%s'  %(i[0][0],i[0][1],i[0][2],i[1],n))
            num = i[1]
            n +=1
        elif i[1] == num:
            print ('%-10s%20s%5s%10s' %(i[0][0],i[0][1],i[0][2],i[1]))


