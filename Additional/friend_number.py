# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 20:22:13 2017

@author: dddda
"""
def sum(x):
    sum = 0
    for i in range (1, x):
        if x % i == 0:
            sum += i
            
    return sum
    
for i in range (1, 10000):
    suma_i = sum(i)
    j = suma_i
    suma_j = sum(j)
    
    if suma_j == i and i != j:
            print(i, j)