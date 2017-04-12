# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 13:37:52 2017

@author: Анастасия
"""

annual_salary = int(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a demimal:'))
total_cost = int(input('Enter the cost of your dream home:'))  
current_saving = 0
numbers_of_months = 0
r = 0.04
portion_down_payment = 0.25 #сколько реально нужно собрать первій взнос total_cost * portion_down_payment

min_sum = portion_down_payment * total_cost

if portion_saved > 1:
    print('pease enter number from 0.1 to 1 ') 
elif portion_saved < 0.1:
    print('It is should be at least 10%')  
montly_salary = annual_salary/12

while current_saving <= min_sum:
    current_saving += montly_salary * portion_saved + (current_saving * r/12)    
    numbers_of_months += 1      
print(numbers_of_months)