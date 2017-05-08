#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
@file: ex1.py
@time: 2017/5/6 17:54
"""

arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,65555]

num1 = 0
num2 = 0
for i in arr:
    if i > num1:
        num1 = i
        for j in arr:
            if j < num2:
                num2 = j
            else:
                num2 = i

print num1, num2