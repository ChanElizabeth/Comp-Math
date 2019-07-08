import numpy as np
import matplotlib.pyplot as plt

#Langrange interpolation equation: P2(x) = y0*l0(x) + y1*l1(x) + y2*l2(x) ......
#l0(x) = (x-x1)/(x0-x1) * (x-x2)/(x0-x2)

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
x_data = np.array([-2, 1, 4, -1, 3, -4])
y_data = np.array([-1, 2, 59, 4, 24, -53])

x = np.linspace(-5, 5, 100)

# plot the figure
fig = plt.figure(1); plt.clf()
ax = fig.add_subplot(1, 1, 1)

ax.plot(x_data, y_data, 'o')
ni = [langrange_intrp(x_data,y_data,i) for i in x]
ax.plot(x, ni, '-')
