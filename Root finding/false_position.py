#For polynomial: 2x^3-3x^2-6
def f(x):
    return 2*x**3-3*x**2-6

def falseposition(x0,x1,e):
    step = 1
    condition = True
    while condition:
      x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
      if f(x0) * f(x2) < 0:
        x1 = x2
      else:
        x0 = x2
      step = step + 1
      condition = abs(f(x2)) > e
    print('root =', x2)

x0 = 1
x1 = 3
e = 1e-5
if f(x0) * f(x1) > 0.0:
    print('wrong limits')
else:
    falseposition(x0,x1,e) 
    
#plot
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,200)
def f(x):    
  return 2*x**3-3*x**2-6
plt.xlabel('x'); plt.ylabel('f(x)'); plt.ylim([-20,20])
plt.axhline(y=0,color='black',linewidth=1.3);plt.axhline(y=0,color='grey')
plt.plot(x,f(x))
