#to differentiate function sin(x) from 0 to 2pi
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
dyf = np.zeros(len(x))
for i in range(len(y)-1):
    dyf[i] = (y[i+1] - y[i])/(x[i+1]-x[i])
print(dyf[-1])
plt.plot(x,dyf,linewidth=2.0, label = 'ff(x)')
plt.plot(x,y,linewidth=2.0, label ='f(x)')
plt.legend()
