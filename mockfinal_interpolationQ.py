#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:09:18 2019

@author: elizabethchan
"""

import numpy as np

#method to find the 'a' value
def coef(x,y):
    n = len(x)
    a = y
    for i in range(1,n):
        a[i:n] = (a[i:n] - a[i-1])/ (x[i:n]-x[i-1])
    return a

#method to find the 'y' value using newton interpolation
def newton_intp(xd,yd,x):
    a = coef(xd, yd)
    n = len(xd) -1
    y = a[n]
    
    for k in range(1, n+1):
        y = a[n-k] + (x-xd[n-k]) * y
    return y

# method of langrange interpolation
def langrange_intrp(xd, yd, x):
    n = np.zeros(len(xd))

    for i in range(0, len(xd)):
        y = 1
        for j in range (0, len(xd)):
            if i != j:
                y = y * (x-xd[j]) / (xd[i]-xd[j])
        n[i] = y

    return np.sum([yd[x] * n[x] for x in range(len(xd))])



# the data
x_data = np.array([44, 46])
y_data = np.array([0.965689, 1.035530])

print("Langrange Interpolation: ", langrange_intrp(x_data, y_data, 45))
print("Newton Interpolation: ", newton_intp(x_data, y_data, 45))

