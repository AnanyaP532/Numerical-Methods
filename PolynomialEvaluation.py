#synthetic division
pol= [6,12,2,25]                         #for solving polynomial 6x^3 + 12x^2 + 2x + 25
x= len(pol)-1                            
n= len(pol)
result=0
for i in range (0,n):
    result= pol[i]+ result*x
print(result)



#Reading files
from numpy import loadtxt
pol = loadtxt("polynomials.txt")
x= len(pol)-1
n= len(pol)
result=0
for i in range (0,n):
    result= pol[i]+ result*x
print(result)
print(pol)
