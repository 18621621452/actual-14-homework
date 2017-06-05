#encoding:utf-8
# 按照多维度ip url status 数据统计及
# 以html格式显示数据

def count():
    count = {}
    # 打开文件
    f = open('www.log','r')
    # 遍历文件及统计数据
    for row in f:
        arr = row.split()
        #print arr
        ip = arr[0]
        url = arr[6]
        status = arr[8]
        count[(ip,url,status)] = count.get((ip,url,status),0)+1
    return count
    # 关闭文件
    f.close()

def result():
    # 获取函数count()统计结果集,然后将字典转换成列表
    arr = count().items()
    return sorted(arr, key=lambda x:x[1],reverse=True)[:10]

def create_html():
    # 将top10数据以html格式显示
    # 获取top10的结果集
    res = result()
    f = open("result.html", "w")
    output = "<table align='center' border=1> \n"
    output += "<tr><td>IP</td><td>url</td><td>status</td><td>count</td></tr> \n"
    for item,count in res:
        ip, url, status = item
        v = count        
        output += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr> \n"%(ip, url, status , v)
    output += "</table>"
    f.write(output)     
    f.close()
create_html()
