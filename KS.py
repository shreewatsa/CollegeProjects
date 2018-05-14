#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:15:08 2018

@author: manjaro
"""
# Kolmogorov-Smirnov (KS) Test
def KSTest():
    print('Enter the numbers : ')
    data = []
    while True:
        try:
            temp = float(input())
        except ValueError:
            break
        data.append(temp)
    print('Given data : ' , data)
    data.sort()
    DPlusList = []
    DMinusList = []
    N = len(data)
    for i in range(1 , N):
        DPlusList.append( i/N - data[i-1] )
        DMinusList.append( data[i-1] - (i-1)/N )
    obs = max(DPlusList + DMinusList )
    print('Dtab value : ' , obs)
    
# Running the KS Test .
KSTest()