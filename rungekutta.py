import matplotlib.pyplot as plt
import numpy as np
# RK-4 python
# EDO
def f(x,y):
    return -y/4 + 1


# metodo de runge-kutta de 4 ordem
def rk4(x0,y0,h,n):
    
    print('\n--------METODO DE RUNGE-KUTTA DE 4 ORDEM--------')
    
    
    print('\n--------SOLUCAO--------')
    print('-------------------------')    
    print('x0\ty0\tyn')
    print('-------------------------')
    valores_t = [x0]
    valores_v = [y0]

    for i in range(n):

        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h/2), (y0+k1/2)))
        k3 = h * (f((x0+h/2), (y0+k2/2)))
        k4 = h * (f((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
        print('%f\t%f\t%f'% (x0,y0,yn) )
        print('-------------------------')
        y0 = yn
        x0 = x0+h
        valores_t.append(x0)
        valores_v.append(y0)
    print('\npara t=%f, v=%f' %(h*n,yn))
    return valores_t, valores_v

# Inputs
print("Nesse caso t0=0 e v0=8\n")
print('Condicoes iniciais:')
x0 = float(input('t0 = '))
y0 = float(input('v0 = '))

print("Nesse caso h=0.1\n")
print('Passo: ')
h = float(input('h = '))

print("n=1000 gera valores suficientes\n")
print('Quantidade de iteracoes:')
step = int(input('n = '))

# chamada rk4
valores_t, valores_v = rk4(x0,y0,h,step)
plt.xlim(0, 40)
plt.ylim(0, 10)
plt.plot(valores_t, valores_v)
plt.xlabel('t')
plt.ylabel('v')
plt.title('Metodo de Runge-Kutta de 4 ordem')
plt.grid(True)
plt.savefig("rk4.png")