#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:19:14 2018

@author: manjaro
"""
# Random Number Generation
# LCS (Linear Congruential Method)

# Formula for generating random numbers using LCG method .
def RandGen(seed ,a = 1 ,c = 0 ,n = 0 ,m = 100):
    X = []
    R = []
    for i in range(n):
        temp = (a * seed + c )% m
        X.append(temp)
        seed = temp
        R.append( X[i] / m )
    return (X , R)

# Taking the inputs and displaying the random numbers .
def LCG():
    print()
    print('LCG has the form :')
    print('Xi = (a * X0 + c) mod m')
    print()
    seed = int(input('Enter the seed value : '))
    n = int(input('Desired number of random numbers : '))
    m = int(input('Enter the modulus value : '))
    choice = input("Enter A for Additive , M for Multiplicative to specify , default is mixed ")
    if(choice is 'A'):   
        c = int(input('Enter constant incrementer , c : '))
        result = RandGen(seed , c = c , n = n , m = m )
    elif(choice is 'M'):
        a = int(input('Enter constant multiplier , a : '))
        result = RandGen(seed , a = a , n = n , m = m )
    else:
        c = int(input('Enter constant incrementer , c : '))
        a = int(input('Enter constant multiplier , a : '))
        result = RandGen(seed , a , c , n = n , m = m )
    X , R = result
    print()
    print('Random Numbers are : ' , X)
    print('Random Numbers between 0 and 1 are : ' , R)
     
# Calling the LCG() function
LCG()
