#for equation dy/dx = 1 - y**2
def f(x,y):
    return 1-y**2

def RK4(x0,y0,xn,n):
    h = (xn-x0)/n
    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h/2), (y0+k1/2)))
        k3 = h * (f((x0+h/2), (y0+k2/2)))
        k4 = h * (f((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
        #print(x0,',',y0,',', yn) 
        y0 = yn
        x0 = x0+h
    print(xn,',',yn)

x0 = 0
y0 = 0
xn = 1
n = 10
RK4(x0,y0,xn,n)
