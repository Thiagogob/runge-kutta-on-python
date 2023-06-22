# RK-4 method python program
import math
# function to be solved
def f(x,y):
    return 2*x - 3*y + 1

# or
# f = lambda x: x+y

# RK-4 method
def rk4(x0,y0,xn,n):
    
    # Calculating step size
    h = (xn-x0)/n
    
    print('\n--------SOLUTION--------')
    print('-------------------------')    
    print('x0\ty0\tyn')
    print('-------------------------')
    for i in range(n):
        k1 = (f(x0, y0))
        k2 = (f((x0+h/2), (y0+k1*h/2)))
        k3 = (f((x0+h/2), (y0+k2*h/2)))
        k4 = (f((x0+h), (y0+k3*h)))
        k = (k1+2*k2+2*k3+k4)*(h/6)
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f'% (x0,y0,yn) )
        print("k1 = %f, k2 = %f, k3 = %f, k4 = %f, k = %f" % (k1, k2, k3, k4, k))
        print('-------------------------')
        y0 = yn
        x0 = x0+h
    
    print('\nAt x=%.4f, y=%.4f' %(xn,yn))

# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

print('Enter number of steps:')
step = int(input('Number of steps = '))

# RK4 method call
rk4(x0,y0,xn,step)