#https://www.python-course.eu/matplotlib_contour_plot.php
import numpy as np
import matplotlib.pyplot as plt

#to make the contour data
xlist = np.linspace(-5, 5, 100)
ylist = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = (X-1)**2 + (8 * ((Y-1)**2))

def obj(x):
    x1 = x[0]
    x2 = x[1]
    f = (x1 - 1)**2 + 8*(x2 - 1)**2
    g = np.array([2*(x1-1), 16*(x2 - 1)]) #first derivative
    H = np.array([[2, 0], [0, 16]]) #Hessian matrix
    return f, g, H


def steepest(obj, x):
    xM = np.zeros((5, 2))
    a = 0.05
    for i in range(5):
        f, g, H = obj(x)
        s = -g
        x = x + a*s
        xM[i] = x
    return xM

def newton(obj, x):
    xM = np.array([x])
    a = 0.02
    while True:
        f, g, H = obj(x)
        s = -g
        x = x + np.linalg.inv(H).dot(s)
        xM = np.vstack((xM, x))
        if(np.linalg.norm(s) < 1.0E-6): break
    return xM

def quasi(obj, x):
    A = np.eye(2)
    c = obj(x)[1]
    a = 0.01
    xv = np.array([x])
    while (np.linalg.norm(c) > 1.0E-6):
        c = obj(x)[1]
        d = -A.dot(c)
        x = x + a * d
        s = a * d
        ck = obj(x)[1]
        y = ck - c
        z = A.dot(y)
        B = np.outer(s, s) / s.dot(y)
        C = -np.outer(z, z) / y.dot(z)
        A = A + B + C
        xv = np.vstack((xv, x))
    return xv

Xinit = np.array([2, 0])
res = steepest(obj, Xinit)
nres = newton(obj, Xinit)
qres = quasi(obj, Xinit)
      
#plot the figure  
fig = plt.figure()
ax = fig.add_subplot(111)
levels = [5, 10, 25, 50, 100]
cp = plt.contour(X, Y, Z, levels)
ax.clabel(cp, inline=True, 
          fontsize=10)
ax.plot(1, 1, "ok")
ax.plot(2, 0, "or")
ax.plot(res[:,0], res[:,1], "ob-", label = "Steepest Descent")
ax.plot(nres[:, 0], nres[:, 1], "-r", label = "Newton's Method")
ax.plot(qres[:, 0], qres[:, 1], "-", label = "Quasi-Newton methods")

ax.set_title("Contour Plot")
ax.set_xlabel("x (cm)")
ax.set_ylabel("y (cm)")
ax.legend(loc = "lower center")
