import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('potential.txt')
x = data[:,0]
y = data[:,1]
dyc = np.zeros(len(x))
for i in range(1,len(y)-1):
    dyc[i] = (y[i+1] - y[i-1])/(x[i+1]-x[i-1])
print(dyc[-1])
plt.plot(x,dyc,linewidth=2.0, label = 'Force')
plt.plot(x,y,linewidth=2.0, label = 'Potential')
plt.legend()
