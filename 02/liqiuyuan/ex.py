#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
@file: ex.py
@time: 2017/5/15 10:22
"""

arr = [87, 15, 64, 55, 11, 100, 54, 77, 48, 15, 65, 74, 90]

for i in range(len(arr)):
    k = arr[i]
    j = i - 1
    while j >= 0:
        if arr[j] > k:
            arr[j+1] = arr[j]
            arr[j] = k
        j -= 1
        print arr