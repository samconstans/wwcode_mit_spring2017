# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:25:13 2017

@author: Анастасия
"""

s = 'bobjdjdfbobobfkfkbob'

count = 0
countBob = 0

for letter in s:
    count += 1
    if (count+1) < len(s) and letter == 'b' and s[count] == 'o' and s[count+1] == 'b':
        countBob += 1
print('Number of times bob occurs is: ' + str(countBob))
