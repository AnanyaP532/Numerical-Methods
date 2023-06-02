import numpy as np
import matplotlib.pyplot as plt
#n = int(input("number of data points:"))
#x = np.zeros(n)
#y = np.zeros(n)
#print("Enter data:")
#for i in range(n):
    #x[i] = float(input("x["+str(i)+"]= "))
    #y[i] = float(input("y["+str(i)+"]= "))
#here we take an example of 3 data points
x = [1,2,3]
y = [3,2,9]
n = len(x)
sumX,sumX2,sumY,sumXY = 0,0,0,0
for i in range(n):
    sumX = sumX + x[i]
    sumX2 = sumX2 + x[i]*x[i]
    sumY = sumY + y[i]
    sumXY = sumXY + x[i]*y[i]

b = (n*sumXY-sumX*sumY)/(n*sumX2-sumX*sumX)
a = (sumY - b*sumX)/n

print('y', '=', a, '+', b,'x')
xco=np.linspace(x[0],x[-1],100)
plt.plot(x,y,'.')
plt.plot(xco,a+b*xco)
