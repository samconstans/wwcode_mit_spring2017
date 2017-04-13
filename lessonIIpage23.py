# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:16:16 2017

@author: Анастасия
"""
import math

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2 - x) >= epsilon:
    if guess <=x:
        guess +=step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded:' + ' ' +str(guess) )