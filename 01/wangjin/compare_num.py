#!/usr/bin/python

NumList = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,46,33,45]

max_num = 0
sec_num = 0

for n in range(len(NumList)):
    if max_num < NumList[n]:
        sec_num = max_num
        max_num = NumList[n]


print ('The bigest NUM is : %s' %(max_num))
print ('The second one is : %s' %(sec_num))
