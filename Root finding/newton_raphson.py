#For equation: x^3+ 6x^2+ 10x +1 = 0

import numpy as np 
import matplotlib.pyplot as plt
tol = 1e-5
x=np.linspace(-5,10,200)
def f(x):     
  return x**4-6*x**2+10*x+1
def f_prime(x):   
  return 4*x**3-12*x+10

def newton(f, df, x0, tol):  
    if f(x0) < tol:
        return x0
    else:
        #print(x0)
        return newton(f, df, x0 - f(x0)/df(x0), tol)
a = np.arange(-10,2,0.5)
#print(a)
value =[]
for i in range(len(a)):
  if (f_prime(a[i]))> 0:
    value.append(a[i])
print(value)
root =[]
for i in range(len(value)):
  root = newton(f,f_prime,value[i], 1e-5) 
print(root)

#plot for function and visualisation

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,200)
def f(x):    
  return x**4-6*x**2+10*x+1
plt.xlabel('x'); plt.ylabel('f(x)'); plt.ylim([-20,20])
plt.axhline(y=0,color='black',linewidth=1.3);plt.axhline(y=0,color='grey')
plt.plot(x,f(x))
