import numpy as np

#1. newton function for root finding 
def newton(f, df, x):
    while True:
        x = x - f(x)/df(x)
        if np.abs( f(x) ) < 1.0E-6: break
    return x

#2. bisection method for root finding
def bisection(f, xl, xu):
    if f(xl)*f(xu) < 0:
        while True:
            xm = 0.5 * (xl+xu)
            if f(xl)*f(xm) < 0:
                xu = xm
            else: 
                xl = xm
                
            if np.abs(f(xm)) < 1.0E-6:
                break
    return xm
    
f = lambda x: x**2 - 2
df = lambda x: 2*x
x0 = 4
x = newton(f, df, x0)

xl = 0; xu = 4
x2 = bisection(f, xl, xu)