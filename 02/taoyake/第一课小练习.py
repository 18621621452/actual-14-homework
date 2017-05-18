小练习1：
用户输入两个数，求平均值
提示int(str)可以把字符串转成数字类型
number_one = raw_input('Please input the first number: ')
number_two = raw_input('Please input the second number: ')
print (int(number_one)+int(number_two))/2.0


小练习2：
让用户一直输入数字，如果输入的是'0',终止程序
打印所有数字之和

sum_one = 0
while sum_one:
    number = raw_input('Please input a number: ')
    if number != '0':
    	sum_one = sum_one + int(number)
    else:
        break

 小练习3：
 让用户一直输入数字(只输入数字)
 如果没有输入任何值，终止程序；
 打印所有输入数字的平均值

 count = 0
 input_num = 0
 is_continue = True
 while is_continue:
     num = raw_input('Please input a number: ')
     if not num or int(num) == 0:
         is_continue = False
     else:
         input_num = input_num + 1.0
         count = count+int(num)
print 'avg is %s' %(count/input_num)

小练习4：
存10000块钱，年利率是3.25%
求多少年之后，存款能翻一番

money = 10000
rate = 0.0325
year = 0

while money <=20000:
    money *= (1+rate)
    year += 1

print money,year


小练习5：
遍历一个序列[‘js’,'C','python','js','css','js','html','node']
统计这个序列中，js出现的次数

List = ['js','C','python','js','css','js','html','node']
k = 0
for i in List:
    if i == 'js':
        k = k + 1
print k


小练习6：
一个序列
[1,2,4,5,3,5,2,8,5,33,25,12,34,89,56,77,43,52]
求这个list的最大值

List = [1,2,4,5,3,5,2,8,5,89,33,25,12,34,89,56,77,43,52]
k = 0
for i in List:
    if k < i:
        k = i
print k

小练习7
用户输入数字判断是不是闰年
如果是100的倍数，要被400整除
被4整除
比如1900不是闰年，2000，2004是闰年
如果输入不是闰年，提示信息，并且继续输入

while True:
    year = raw_input('input a num : ')
    if not year:
        break
    year = int(year)
    if year%400==0 or (year%100>0 and year%4==0)
        print '%s is leap year' %(year)
    else:
        print '%s is not leap year' %(year)
                







