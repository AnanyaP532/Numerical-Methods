import numpy as np
import matplotlib.pyplot as plt
x = np.array([-1,0,3,6])                    #data point x
y = np.array([3,-6,39,822])                 #data point y
n = 4
xp = np.linspace(-1,6)
yp= np.zeros([])
for i in range(n):
  p = 1
  for j in range(n):
    if i != j:
      p = p * (xp - x[j])/(x[i] - x[j])
  yp = yp + p * y[i]    

print(xp[-1], ',', yp[-1])

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo')
plt.plot(xp, yp)

#reading files
import numpy as np
data = np.loadtxt('interpolation.txt')
x = data[:,0]
y = data[:,1]
n = len(x)
xp = 7
yp = 0

for i in range(n):
  p = 1
  for j in range(n):
    if i != j:
      p = p * (xp - x[j])/(x[i] - x[j])
  yp = yp + p * y[i]    

print(xp, ',', yp)
