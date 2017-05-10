list=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
m=0
for i in list:
    if m < i:
        m = i
n=0
for j in list:
    if n < j and j != m:
        n = j
print m,n
