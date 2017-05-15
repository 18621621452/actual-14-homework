#coding=utf-8
arr = [10,4,3,11,1,2,6,5,12,9,7,8]
print arr
length = len(arr)
print "length=%s" %length
# for i in range(1,length):
#     print "-"*50
#     for j in range(i):
#         print "%s与%s比较" %(arr[i],arr[j])
#         if arr[i] < arr[j]:
#             arr[i],arr[j]=arr[j],arr[i]
#             print "%s swap %s" %(arr[i],arr[j])
#         print arr
# print arr


for i in range(1,length):
    print "-"*50
    tmp = arr[i]
    for j in range(i-1,-1,-1):
        print "%s拿出与%s比较" %(tmp,arr[j])
        if tmp < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = tmp
            print "%s后移到第%s位,%s放到第%s位" %(arr[j+1],j+1,arr[j],j)
        else:
            break
    print arr
print arr
