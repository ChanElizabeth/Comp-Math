#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 21:05:11 2019

@author: elizabethchan
"""

import numpy as np

def obj(x):
    x0 = x.item(0)
    print("x0: ", x0)
    x1 = x.item(1)
    print("x1: ",x1)
    f = 2*x0*x1 + 2*x0 + x0**2 - 2*x1**2
    g = np.array([[2*x1 + 2 + 2*x0, 2*x0 - 4*x1]])
    H = np.array([[2,4],[4,-4]])
    return f,g,H

def steepest(obj,x):
    j = 0
    a = 0.1
    xv = np.array([x])
    for i in range(0, 10):
        f, g, h = obj(x)
        s = -g
        #print("Iteration ", j, " ", s, " ", x, " ", f)
        print("f(x): ", f)
        print("Iteration ", j, "\n")
        j = j + 1
        if np.linalg.norm(s) < 1.0E-6:
            break
        x = x + a * s
        xv = np.vstack((xv,x))
    return xv

x = np.array([0.5, 1])
result = steepest(obj, x)

#def steepest(f, x0, x1, n, a):
#    fx = np.ones(n)
#    x = np.ones(n)
#    y = np.ones(n)
#    fx[0] = f(x0, x1)
#    x[0] = x0
#    y[0] = x1
#    for i in range(1, n):
#        gx = 2*y[i-1] + 2 + 2*x[i-1]
#        gy = 2*x[i-1] - 4*y[i-1]
#        x[i] = x[i-1] - a * gx
#        y[i] = y[i-1] - a * gy
#        fx[i] = f(x[i], y[i])
#    return x, y, fx
#
#x0 = 0.5
#x1 = 1.0
#f = lambda x0, x1 : 2*x0*x1 + 2*x0 + x0**2 - 2*x1**2
#print(steepest(f, x0, x1, 10, 0.1))