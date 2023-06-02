#The set of equations to be solved:
#15x + y - 2z = 6 --> (6-y+2*z)/15
#3x + 20y -2z = -12 --> (-12-3*x+2z)/20
#2x - 3y + 18z = 25 --> (25-2x+3y)/18

N=5 
x=0;y=0;z=0
for i in range(N):
  x = (1/15)*(6-y+2*z)
  y = (1/20)*(-12-3*x-2*z)
  z = (1/18)*(25-2*x-3*y)
print('x',x)
print('y',y)
print('z',z)
