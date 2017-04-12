# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 13:37:52 2017

@author: Анастасия
"""

import math

annual_salary = float(input('Enter your annual salary:'))
portion_saved = input('Enter the percent of your salary to save, as a demimal:')
current_saving = 0


if float(portion_saved) > 1:
    print('pease enter number from 0.1 to 1 ') 
elif float(portion_saved) < 0.1:
    print('It is should be at least 10%')    
else:
    current_saving = float(annual_salary) * float(portion_saved)
        
portion_down_payment = 0.25 #сколько реально нужно собрать первій взнос total_cost * portion_down_payment

total_cost = float(input('Enter the cost of your dream home:'))    
        
r = 0.04  
investments = float(current_saving)* r/12

base = 1 + r/12

print('base',base)

A0 = int((total_cost * portion_down_payment)/(annual_salary * portion_saved))


print('portion_down_payment/annual_salary*portion_saved',A0)


numbers_of_months = math.log(A0, base)/5

print(int(numbers_of_months))
