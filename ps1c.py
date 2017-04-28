# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 13:26:07 2017

@author: Анастасия
"""

total_cost = 1000000
portion_down_payment = 0.25
annual_salary = int(input('Enter your starting annual salary:'))
min_sum = portion_down_payment * total_cost #250 000
#portion_saved = float(input("Enter your portion saved:"))
steps = 0
low = 0
high = 1
epsilon = 100 #-+100$ from total cost

def calculation_of_savings(annual_salary, portion_saved): #current_savings_36_months
    current_saving = 0
    numbers_of_months = 0
    r = 0.04
    semi_annual_raise = 0.07
    montly_salary = annual_salary/12
    
    while numbers_of_months < 36:
        current_saving += montly_salary * portion_saved + (current_saving * r/12)
        numbers_of_months += 1
        if numbers_of_months%6 == 0:        
            montly_salary +=  montly_salary * semi_annual_raise
    return current_saving

def check(a):
    if a > 0:
        i = 1
    if a < 0:
        i = -1
    else:
        i = 0
    return i


if calculation_of_savings(annual_salary, high) < min_sum:
    print('It is not possible to pay the down payment in three years.')
else:
    while True:
        steps +=1
        guess = (high + low)/2
        total_saved_low = calculation_of_savings(annual_salary, low)
        total_saved_high = calculation_of_savings(annual_salary, high)
        total_saved_guess = calculation_of_savings(annual_salary, guess)
        if abs(min_sum - total_saved_guess) < epsilon:
            print('Beat savings rate: {0:6.4f}'.format(guess))
            print('Steps in bisection search: ',steps)
            break
        elif check(min_sum - total_saved_low) != check(min_sum - total_saved_guess) < 0:
            high = guess
        else:
            low = guess
    
    