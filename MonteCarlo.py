#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:22:48 2018

@author: manjaro
"""

import numpy as np
import matplotlib.pyplot as plt

c = 0
s = 0
pi = []
n = 1000
xIndex = []
yIndex = []
xCircle = []
yCircle = []
xyPos = []
for i in range(n):
    x , y = np.random.uniform( -1 , 1 , size = 2)
    xIndex.append(x)
    yIndex.append(y)
    s += 1
    pos = x**2 + y**2
    xyPos.append(pos)
    if(pos <= 1):
        c += 1
        xCircle.append(x)
        yCircle.append(y)
    pi.append(4*c/s)
    
print(pi[n-1])
plt.plot(pi)
plt.axhline(3.14159, color='green')


plt.scatter(xIndex, yIndex , c = 'red' , s = 5, label = 'Outside circle')
plt.scatter(xCircle, yCircle, c =  'green' , s = 5, label = 'Inside circle')
plt.title('Plotting random points')
plt.legend()
plt.show()


# Uniform distribution of random numbers .
XX = np.random.uniform(-1 , 1 , size = 10000)
plt.hist(XX)


# Experiment section
#for i in range(1000):
#    plt.scatter(xIndex[i], yIndex[i], c= ('red' if xyPos[i] < 1 else 'green') , s= 5)
#
