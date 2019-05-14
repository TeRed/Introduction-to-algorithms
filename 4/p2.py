# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:38:10 2017

@author: dddda
"""
import math
import time

width = int(input("Podaj szerokosc: "))
height = int(input("Podaj wysokosc: "))

write = [math.floor(width/2), math.floor(width/2), math.floor(height/2), math.floor(height/2)]
expand = True

while True:
    for i in range (0, height):
        for j in range (0, width):
            if (j == write[0] or j == write[1]) and i >= write[2] and i <= write[3]:
                print("X", end="")
            elif (i == write[2] or i == write[3]) and j >= write[0] and j <= write[1]:
                print("X", end="")
            else: print("O", end="")
        print("")
        
    if(write[0] == 0 or write[2] == 0): expand = False
    if(write[0] == write[1] and write[2] == write[3]): expand = True
    if expand:
        write[0] -= 1
        write[1] += 1
        write[2] -= 1
        write[3] += 1
    else:
        write[0] += 1
        write[1] -= 1
        write[2] += 1
        write[3] -= 1

    time.sleep(0.3)
    print("")