#encoding:utf-8
print "------------选择排序------------"

lstA=[1,5,2,9,0,3,21,-2]
print "排序前：",lstA
leng=len(lstA)

for index in range(leng-1): 
    n=index+1
    for i in range(n,leng):
        if lstA[index]>lstA[i]:
            lstA[index],lstA[i]=lstA[i],lstA[index]

print "排序后：",lstA


print "------------冒泡排序------------"
lstA=[1,5,2,9,0,3,21,-2]
print "排序前：",lstA
leng=len(lstA)
for index in range(leng-1):     
    for i in range(leng-1-index):
        if lstA[i]>lstA[i+1]:
            lstA[i],lstA[i+1]=lstA[i+1],lstA[i]

print "排序后：",lstA