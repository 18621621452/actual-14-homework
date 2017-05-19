#!/usr/bin/env python
# coding:utf-8
#定义一个List列表 
List = [8,20,12,5,30,200,55,89,37,69,203,106,112,25,21,13,205,7]
#把列表的元素个数赋值给一个变量
Count = len(List) 
#遍历列表中所有的元素下标
for i in range(1,Count):
    k = List[i]    #遍历列表之后得到的元素下标赋值给k
    j = i - 1      #定义变量j为列表元素的上一位
    while j >=0:   #如果j大于等于0
        if List[j] > k:              #如果如果列表中元素j的值大于k的值，
            List[j + 1] = List[j]    #那么j+1的值就是j的值     
            #print List[j+1]
            #print [j]
            List[j] = k              #列表元素j等于k
        j = j - 1                    #j循环一次减去1
print List
