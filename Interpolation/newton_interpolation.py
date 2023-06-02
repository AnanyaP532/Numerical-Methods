import numpy as np
import matplotlib.pyplot as plt
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    for j in range(1,n):
      for i in range(n-j):
        coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
    return coef

def newton_poly(coef, x_data, x):
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p
x = np.array([-5, -1, 0, 2])                     #data point for x
y = np.array([-2, 6, 1, 3])                      #data point for y
a_s = divided_diff(x, y)[0, :]
x_new = np.arange(-5, 2.1, .1)
y_new = newton_poly(a_s, x, x_new)
xp = -2.5
yp =  newton_poly(a_s, x, xp)
print(xp, ',', yp)
#ploting the interpolation curve
plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, y_new)
