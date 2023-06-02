#to diffentiate function sin(x) from 0 to 2pi
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
dyb = np.zeros(len(x))
for i in range(1,len(y)):
    dyb[i] = (y[i] - y[i-1])/(x[i]-x[i-1])
print(dyb[-1])
plt.plot(x,dyb,linewidth=2.0, label = 'fb(x)')
plt.plot(x,y,linewidth=2.0, label = 'f(x)' )
plt.legend()
