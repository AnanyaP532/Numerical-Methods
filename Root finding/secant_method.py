#For polynomial: 4x^4 + 5x^2 -9

def f(x):
    return 4*x**4 - 5*x**2 - 9

def secant(x0,x1,e,N):
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('error')
            break
        else:
          x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
          x0 = x1
          x1 = x2
          step = step + 1
        
          if step > N:
            print('Non Convergent')
            break
        
          condition = abs(f(x2)) > e
    print('root =', x2)

x0 = 1
x1 = 2
e = 1e-6
N = 10

secant(x0,x1,e,N)

#function visualisation

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,200)
def f(x):    
  return 4*x**4 - 5*x**2 - 9
plt.xlabel('x'); plt.ylabel('f(x)'); plt.ylim([-20,20])
plt.axhline(y=0,color='black',linewidth=1.3);plt.axhline(y=0,color='grey')
plt.plot(x,f(x))
