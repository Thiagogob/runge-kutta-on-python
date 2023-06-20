import matplotlib.pyplot as plt
import numpy as np
# RK-4 python
# EDO
def f2(t,v2):
    return -v2/4 + 1

def f1(t,v2,v1):
    return -v1/4 + v2/4 + 1

# metodo de runge-kutta de 4 ordem
def rk4(t0,v2_0,v1_0,h,n):
    
    print('\n--------METODO DE RUNGE-KUTTA DE 4 ORDEM--------')
    
    
    print('\n--------SOLUCAO--------')
    print('-------------------------')    
    print('x0\ty0\tyn')
    print('-------------------------')
    valores_t = [t0]
    valores_v2 = [v2_0]
    valores_v1 = [v1_0]

    for i in range(n):

        k1 = h * (f2(t0, v2_0))
        k2 = h * (f2((t0+h/2), (v2_0+k1/2)))
        k3 = h * (f2((t0+h/2), (v2_0+k2/2)))
        k4 = h * (f2((t0+h), (v2_0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        v2_n = v2_0 + k
        print('%f\t%f\t%f'% (t0,v2_0,v2_n) )
        print('-------------------------')
        v2_0 = v2_n




        k1 = h * (f1(t0, v2_0,v1_0))
        k2 = h * (f1((t0+h/2), v2_0,(v1_0+k1/2)))
        k3 = h * (f1((t0+h/2), v2_0,(v1_0+k2/2)))
        k4 = h * (f1((t0+h), v2_0,(v1_0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        v1_n = v1_0 + k

        v1_0 = v1_n
        t0 = t0+h


        valores_t.append(t0)
        valores_v1.append(v1_0)
        valores_v2.append(v2_0)

    print('\npara t=%f, v=%f' %(h*n,v2_n))
    return valores_t, valores_v1, valores_v2

# Inputs
def main():
    print("Nesse caso t0=0 v2_0=8 e v1_0=12\n")
    print('Condicoes iniciais:')
    t0 = float(input('t0 = '))
    v1_0 = float(input('v1_0 = '))
    v2_0 = float(input('v2_0 = '))

    print("Nesse caso h=0.1\n")
    print('Passo: ')
    h = float(input('h = '))

    print("n=1000 gera valores suficientes\n")
    print('Quantidade de iteracoes:')
    step = int(input('n = '))

    # chamada rk4
    valores_t, valores_v1,valores_v2 = rk4(t0,v2_0,v1_0,h,step)
    plt.xlim(0, 40)
    plt.ylim(0, 20)
    plt.plot(valores_t, valores_v2)
    plt.plot(valores_t, valores_v1)
    plt.xlabel('t')
    plt.ylabel('v')
    plt.title('Estado de escoamento dos tanques')
    plt.grid(True)
    plt.savefig("rk4.png")

if __name__ == "__main__":
    main()