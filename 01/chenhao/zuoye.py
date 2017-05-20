List = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
Max1 = 0
Max2 = 0

for i in List:
    if i > Max1:
        Max1 = i
    for o in List:
        if Max2 < o and o < Max1:
            Max2 = o
print 'The max number is :',Max1
print 'The second number is:',Max2
