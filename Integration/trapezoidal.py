#integrating function sin(x**2) from 0 to 1
import numpy as np
def f(x):
    return np.sin(x**2)

def trapezoidal(x0,xn,n):
    h = (xn - x0) / n
    integ = f(x0) + f(xn)
    for i in range(1,n):
      k = x0 + i*h
      integ = integ + 2 * f(k)
    
    integ = integ * h/2
    return integ
x0 = 0
xn = 1
n = 4
result = trapezoidal(x0,xn,n)
print('Result =', result)

#visualising area under graph
import numpy as np
import matplotlib.pyplot as plt
xcord=np.linspace(x0,xn,100)
plt.ylim([0.0,1.5])
plt.plot(x,f(x),linewidth=2.0,label=r'$f(x)$')
plt.fill_between(xcord,f(xcord))
plt.legend()
