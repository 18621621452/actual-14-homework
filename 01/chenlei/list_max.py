num_list = [1,666666666,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
first = 0
second = 0 

for i in num_list :
    for j in num_list :
        if j > first :
            first = j
    if i > second and i != first :
        second = i 

print num_list
print 'first=%s,second=%s' %(first,second)

