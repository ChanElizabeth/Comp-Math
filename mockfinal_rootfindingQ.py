#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:21:54 2019

@author: elizabethchan
"""
import numpy as np

#1. newton function for root finding 
def newton(f, df, x):
    counter = 0
    while True:
        x = x - f(x)/df(x)
        counter += 1
        if np.abs( f(x) ) < 0.05: break
    return x, counter

#2. bisection method for root finding
def bisection(f, xl, xu):
    counter2 = 0
    if f(xl)*f(xu) < 0:
        while True:
            xm = 0.5 * (xl+xu)
            if f(xl)*f(xm) < 0:
                xu = xm
            else: 
                xl = xm
             
            counter2 += 1
            if np.abs(f(xm)) < 0.05:
                break
    return xm, counter2
    
f = lambda x: x**3 + 7*x**2 - 36
df = lambda x: 3*x**2 + 14*x
x0 = -2
x = newton(f, df, x0)

xl = -4; xu = -2
x2 = bisection(f, xl, xu)

print("(The root, Num of Iterations): ", x)
print("(The root, Num of Iterations): ", x2)