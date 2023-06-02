#The set of equations we use are:
#15x + y - 2z = 6 --> (6-y+2*z)/15
#3x + 20y -2z = -12 --> (-12-3*x+2z)/20
#2x - 3y + 18z = 25 --> (25-2x+3y)/18

import numpy as np
def gaussElim(a,b):
    n = len(b)
    # Elimination phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                #if not null define λ
                lam = a [i,k]/a[k,k]
                #we calculate the new row of the matrix
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                #we update vector b
                b[i] = b[i] - lam*b[k]
                # backward substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    
    return b

#initial coefficients
a=np.array([[15.0,1.0,-2.0],[3.0,20.0,-2.0],[2.0,-3.0,18.0]])
b=np.array([6.0,-12.0,25.0])
x = gaussElim(a,b)
print(a)
print("x =",x)
det = np.prod(np.diagonal(a)) #determinant
print("\ndet =",det)
