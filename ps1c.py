# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 13:26:07 2017

@author: Анастасия
"""

annual_salary = int(input('Enter your starting annual salary:'))
down_payment = 250000.0
error = 100
semi_annual_raise = 0.07
r = 0.04
all_months = 36
left = 0
right = 10000
saving_rate = 0.0
steps = 0
    
while left + 1 < right:
    portion_saved =int((left+right)/2)
    current_savings = 0.0
    monthly_salary = annual_salary / 12
    for month in range(1, all_months+1):
        current_savings += (current_savings * r) / 12 + (
            portion_saved/10000 * monthly_salary)
        if month % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    steps += 1
    difference = current_savings - down_payment
    if 0.0 <= difference < error:
        saving_rate =(left + right)/2
        break
    elif difference < 0:
        left = portion_saved
    elif difference > error:
        right = portion_saved
saving_rate = saving_rate/10000
    
if 0.0 < saving_rate < 1:
    print('Best savings rate:', saving_rate)
    print('Steps in bisection search:', steps)
else:
    print('It is not possible to pay he down payment in three years.')