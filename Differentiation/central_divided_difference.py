#to differentiate sin(x) frpm 0 to 2pi
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
dyc = np.zeros(len(x))
for i in range(1,len(y)-1):
    dyc[i] = (y[i+1] - y[i-1])/(x[i+1]-x[i-1])
print(dyc[-1])
plt.plot(x,dyc,linewidth=2.0, label = 'fc(x)')
plt.plot(x,y,linewidth=2.0, label = 'f(x)')
plt.legend()
