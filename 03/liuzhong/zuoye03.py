#!/bin/env python
# encoding:utf-8
f = open('/root/access.log')
my_dict={}
for l in f:
	i = l.split()[0]
	u = l.split()[10]
	s = l.split()[8]
	my_dict[(i,u,s)]=my_dict.get((i,u,s),0)+1
#print my_dict.items()
my_list = my_dict.items()
length = len(my_list)
for i in range(length-1):
    for j in range(length-1-i):
        if  my_list[j][1] > my_list[j+1][1]:
            my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
for key,val in my_list[:-11:-1]:
    print '%s count is %s'%(key,val)
    
