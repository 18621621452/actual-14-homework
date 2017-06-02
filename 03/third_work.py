count_dict = {}
file_tuple = ()
all_list = []

with open('www_access_20140823.log', 'r') as f:
    for line in f.readlines():
        num = 0
        ip = line.split()[0]
        url = line.split()[10].split('"')[1]
        status = line.split()[8]
        file_tuple = (ip,url,status)
        count_dict[file_tuple] = count_dict.get(file_tuple,0) + 1

all_list = count_dict.items()

length  = len(all_list)
for i in range(length-1):
    for j in range(length-i-1):
        if all_list[j][1] < all_list[j+1][1]:
            all_list[j],all_list[j+1]=all_list[j+1],all_list[j]

for i in range(length-1):
    if all_list[i][1] != all_list[i+1][1]:
        num += 1
    if num == 10:
        index = i
        break

num = 0
for key,value in all_list[0:index+1]:
    num += 1
    print "(%s) ip:%s; url:%s; status:%s; count:%s" %(num,key[0],key[1],key[2],value)