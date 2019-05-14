# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 20:19:10 2017

@author: dddda
"""

i = 1
while True:
    sum = 0
    for x in range (1, i):
        if i % x == 0:
            sum += x
    if sum == i:
        print(i)
    i += 1