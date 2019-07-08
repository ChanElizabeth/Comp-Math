import numpy as np

#function
f = lambda x: x**4 - 3*x**3 + 6*x**2 - 10*x - 9
#exact derivative of the function
df1_exact = lambda x: 4*x**3 - 9*x**2 + 12*x - 10
df2_exact = lambda x: 12*x**2 - 18*x + 12


#function for central difference
def df1_cd(f, x, h):
    df1_cd = (f(x + h) - f(x - h)) / (2 * h)
    return df1_cd

def df2_cd(f, x, h):
    df2_cd = ( f(x+h) - 2*f(x) + f(x-h) ) / (h**2)
    return df2_cd

x = 0
print("Exact first derivative: ", df1_exact(x))
print("Exact second derivative: ", df2_exact(x))

print("First derivative approx (h = 0.5): ", df1_cd(f, x, 0.5))
print("First derivative approx (h = 0.25): ", df1_cd(f, x, 0.25))
print("First derivative approx (h = 0.125): ", df1_cd(f, x, 0.125))

print("Second derivative approx (h = 0.5): ", df2_cd(f, x, 0.5))
print("Second derivative approx (h = 0.25): ", df2_cd(f, x, 0.25))
print("Second derivative approx (h = 0.125): ", df2_cd(f, x, 0.125))

print("First derivative Relative Error (h = 0.5) :", ( np.linalg.norm(df1_cd(f, x, 0.5)-df1_exact(x)) / np.linalg.norm(df1_exact(x)) ) * 100)
print("First derivative Relative Error (h = 0.25) :", ( np.linalg.norm(df1_cd(f, x, 0.25)-df1_exact(x)) / np.linalg.norm(df1_exact(x)) ) * 100)
print("First derivative Relative Error (h = 0.125) :", ( np.linalg.norm(df1_cd(f, x, 0.125)-df1_exact(x)) / np.linalg.norm(df1_exact(x)) ) * 100)

print("Second derivative Relative Error (h = 0.5) :", ( np.linalg.norm(df2_cd(f, x, 0.5)-df2_exact(x)) / np.linalg.norm(df2_exact(x)) ) * 100)
print("Second derivative Relative Error (h = 0.25) :", ( np.linalg.norm(df2_cd(f, x, 0.25)-df2_exact(x)) / np.linalg.norm(df2_exact(x)) ) * 100)
print("Second derivative Relative Error (h = 0.125) :", ( np.linalg.norm(df2_cd(f, x, 0.125)-df2_exact(x)) / np.linalg.norm(df2_exact(x)) ) * 100)
