#integrating function x**2 from 0 to 1
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2,100)
def f(x):
    return x**2

def simpson(x0,xn,n):
    h = (xn - x0) / n 
    integ = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h  
        if i%2 == 0:
            integ = integ + 2 * f(k)
        else:
            integ = integ + 4 * f(k)
    integ = integ * h/3
    return integ
    
x0 = 0
xn = 1
n = 10
xcord=np.linspace(x0,xn,100)
result = simpson(x0,xn,n)
print('result =', (result) )

#plot to visualise the area under function
plt.ylim([0.0,1.5])
plt.plot(x,f(x),linewidth=2.0,color='red',label=r'$f(x)$')
plt.fill_between(xcord,f(xcord),color='blue')
plt.legend()
