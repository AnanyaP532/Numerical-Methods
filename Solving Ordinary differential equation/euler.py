#for function dy/dx = 1 - y**2
def f(x,y):
    return 1-y**2

def euler(x0,y0,xn,n):
    h = (xn-x0)/n
    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope 
        y0 = yn
        x0 = x0+h
    print(xn, ',', yn)
x0 = 0
y0 = 0
xn = 1
n = 10
euler(x0,y0,xn,n)
