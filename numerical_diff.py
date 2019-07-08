import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#function
f = lambda x: np.sin(x)**2
#exact derivative of the function
df_exact = lambda x: 2 * np.cos(x) * np.sin(x)

#function for central difference
def df_cd(f, x, h = 1.0E-5):
    df_cd = (f(x + h) - f(x - h)) / (2 * h)
    return df_cd

#function for backward difference
def df_bd(f, x, h = 1.0E-5):
    df_bd = (f(x) - f(x - h)) / h
    return df_bd

#function for forward difference
def df_fd(f, x, h = 1.0E-5):
    df_fd = (f(x + h) - f(x)) / h
    return df_fd

x = np.linspace(0.0, 1.0, 11)

#plot the figure
fig = plt.figure(1); plt.clf()
ax = fig.add_subplot(111)
ax.plot(x, df_exact(x), label = 'Exact')
ax.plot(x, df_cd(f, x), 'o', label = 'Central')
ax.plot(x, df_bd(f, x), '+', label = 'Backward')
ax.plot(x, df_fd(f, x), 'x', label = 'Forward')
ax.set_xlabel('x')
ax.set_ylabel('df(x)')
ax.legend()

#print the relative error
print("Relative Error of Central Difference: ", ( np.linalg.norm(df_cd(f,x) - df_exact(x)) / np.linalg.norm(df_exact(x)) ) * 100)
print("Relative Error of Forward Difference: ", ( np.linalg.norm(df_fd(f,x) - df_exact(x)) / np.linalg.norm(df_exact(x)) ) * 100)
print("Relative Error of Backward Difference: ", ( np.linalg.norm(df_bd(f,x) - df_exact(x)) / np.linalg.norm(df_exact(x)) ) * 100)
