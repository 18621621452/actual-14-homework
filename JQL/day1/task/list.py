

li = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for m in range(1,len(li)):
    for n in range(len(li)-m):
        num1 = li[n]
        num2 = li[n+1]
        if num1 > num2:
            temp = li[n]
            li[n] = num2
            li[n+1] = temp
print li[-1],li[-2]
