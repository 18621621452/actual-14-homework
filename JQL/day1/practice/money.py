#!/usr/bin/env python
#coding:utf-8
#存10000块钱，年利率3.25% 求多少年后，存款翻倍
year = 0 
money = 10000
while money <20000:
    money = money+money*0.0325
    year = year+1
print money,year
