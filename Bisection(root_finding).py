#For equation: x^4 + x^2 -5

import numpy as np
tol = 1e-6                           
def f(x):
  return (x**4+x**2-5)
gap = 0.5
a = np.arange(-10,10,0.5)
b = a + gap
#print(a)
#print(b)
fil = []                          
for i in range(len(a)):
  if f(a[i]) * f(b[i]) > 0:
    fil.append(i)
#print(fil)
a = np.delete(a,fil)
b = np.delete(b,fil)
print("a=", a)
print("b=", b)
for i in range(len(a)):
    for k in range(len(b)):
        if(f(a[i]) * f(b[k]) < 0):
            c= (a[i] + b[k])/2
            if(f(a[i]) * f(c) < 0):
                b[k] = c
            else:
                a[i] = c
            if(f(c) < tol or f(c) == 0):
                print("Root is", c)
            else:
                continue
               
#Function and root plotting

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,100)
def f(x):
  return(x**4+x**2-5)
plt.xlabel('x');plt.ylabel('f(x)')
plt.ylim([-10,10])
plt.axhline(0,linestyle='--')
plt.axvline(0,linestyle='--')
plt.plot(x,f(x))
