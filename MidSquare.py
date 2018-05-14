#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#MidSquare Method for random number generation

seed = int(input('Enter the seed value :'))
n = int(input('Desired number of random numbers : '))
randNum = []
for i in range(n):
    seed = seed**2
    seed /= 10
    seed = int(seed % 100)
    randNum.append(seed)

# Displaying list of random numbers
print('Generated random numbers are : ' , randNum)
