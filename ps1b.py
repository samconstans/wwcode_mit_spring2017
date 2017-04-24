# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:13:15 2017

@author: Анастасия
"""

import math

annual_salary = int(input('Enter your starting annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = int(input('Enter the cost of your dream home:'))  
semi_annual_raise = float(input('Enter the sem-annual raise, as a decimal:'))

current_saving = 0
numbers_of_months = 0
r = 0.04
portion_down_payment = 0.25 #сколько реально нужно собрать первій взнос total_cost * portion_down_payment



min_sum = portion_down_payment * total_cost - current_saving

"""
if portion_saved > 1:
    print('pease enter number from 0.1 to 1 ') 
elif portion_saved < 0.1:
    print('It is should be at least 10%')  
"""    
    
montly_salary = annual_salary/12



while current_saving <= min_sum:
    current_saving += montly_salary * portion_saved + (current_saving * r/12)
    numbers_of_months += 1
    if numbers_of_months%6 == 0:        
        montly_salary +=  montly_salary * semi_annual_raise
    
print(numbers_of_months)