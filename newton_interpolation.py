import numpy as np
import matplotlib.pyplot as plt

#Newton interpolation equation: y = a0 + a1(x-x0) + a2(x-x0)(x-x1) ......
 
#method to find the 'a' value
def coef(x,y):
    n = len(x)
    a = y
    for i in range(1,n):
        a[i:n] = (a[i:n] - a[i-1])/ (x[i:n]-x[i-1])
    return a

#method to find the 'y' value
def newton_intp(xd,yd,x):
    a = coef(xd, yd)
    n = len(xd) -1
    y = a[n]
    
    for k in range(1, n+1):
        y = a[n-k] + (x-xd[n-k]) * y
    return y

x_data = np.array([-2, 1, 4, -1, 3, -4])
y_data = np.array([-1, 2, 59, 4, 24, -53])

x = np.linspace(-5, 5, 100)


fig = plt.figure(1); plt.clf()
ax = fig.add_subplot(1, 1, 1)

ax.plot(x_data, y_data, 'o')
ni = newton_intp(x_data,y_data,x)
ax.plot(x, ni, '-')
