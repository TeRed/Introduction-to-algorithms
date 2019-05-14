# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 20:58:56 2017

@author: dddda
"""

months = [False, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

week_day = 4
day = 1
year = 2015
year_to_add = 2016
month = 1

while True:
    if year == 2022: break
    if year == year_to_add:
        months[2] = 29
        year_to_add += 4
    
    if(week_day == 5 and day == 13): print(str(day) + " " + str(month) + " " + str(year))
    
    day += 1
    week_day += 1
    if week_day == 8: week_day = 1
    if day > months[month]:
        if month == 12:
            year += 1
            month = 1
            day = 1
            months[2] = 28
            #print(week_day)
            #print(months)
        else:
            day = 1
            month += 1
            