#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:04:32 2018

@author: manjaro
"""

# Drunkard Problem

import numpy as np
import matplotlib.pyplot as plt
f = 40
b = 10
l = 25
r = 25
x = 0
y = 0
xTrack = [0]
yTrack = [0]
step = 0
for i in range(1000):
    rnd = np.random.uniform(0,100)
    if( rnd < 40):
        y += 1
    elif( rnd < 50):
        y -= 1
    elif( rnd < 75):
        x -= 1
    else:
        x += 1
    xTrack.append(x)
    yTrack.append(y)
    step += 1
    if(y == 50):
        print('Steps required : ' , step)
        print('Final Position : (', x , ',' , y , ')' )
        break

plt.plot(xTrack, yTrack)
