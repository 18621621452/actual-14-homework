#coding=utf-8
def html_write(arr):
    with open('res.html', 'w') as f:
        res = "<table border='1'>\n<tr><td>ip</td><td>url</td><td>status</td><td>count</td></tr>\n"
        for key,value in arr:
            print key[0],key[1],key[2],value
            res += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n' %(key[0],key[1],key[2],value)
        res += '</table>'
        f.write(res)

def file_read():
    count_dict = {}
    with open('log.log', 'r') as f:
        for line in f:
            tmp = line.split()
            ip,url,status = tmp[0],tmp[6],tmp[8]
            file_tuple = (ip,url,status)
            count_dict[file_tuple] = count_dict.get(file_tuple,0) + 1
    return count_dict.items()

def ten_index(length,sort_list):
    for i in range(length):
        if i >=10:
            if sort_list[-i-1][1] != sort_list[-i][1]:
                index = i
                break
    return index

all_list = file_read()
sort_list = sorted(all_list,key=lambda x:x[1])
length = len(sort_list)
index = ten_index(length,sort_list)
html_write(sort_list[:-index - 1:-1])
