import matplotlib.pyplot as plt
import numpy as np
# RK-4 python
# EDO
def v2(t,v2):
    return -v2/4 + 1

def v1(t,v2,v1):
    return -(v1/4) + v2/4 + 1

# metodo de runge-kutta de 4 ordem
def rk4(t0,v2_0,v1_0,h,n):
    

    valores_t = [t0]
    valores_v2 = [v2_0]
    valores_v1 = [v1_0]

    for i in range(n):


        #calculando v_1
        k1 = (v1(t0, v2_0,v1_0))
        k2 = (v1((t0+h/2), v2_0,(v1_0+(k1*h/2))))
        k3 = (v1((t0+h/2), v2_0,(v1_0+(k2*h/2))))
        k4 = (v1((t0+h), v2_0,(v1_0+k3*h)))
        k = (k1+2*k2+2*k3+k4)*(h/6)

        #atribuindo um novo valor para v1
        v1_n = v1_0 + k

        v1_0 = v1_n


        #calculando v_2
        k1 = (v2(t0, v2_0))
        k2 = (v2((t0+h/2), (v2_0+(k1*h/2))))
        k3 = (v2((t0+h/2), (v2_0+(k2*h/2))))
        k4 = (v2((t0+h), (v2_0+(k3*h))))
        k = (k1+2*k2+2*k3+k4)*(h/6)

        #atribuindo um novo valor para v2
        v2_n = v2_0 + k


        v2_0 = v2_n


        #atualizando o valor de t
        t0 = t0+h

        #colocando valores em listas
        valores_t.append(t0)
        valores_v1.append(v1_0)
        valores_v2.append(v2_0)

    return valores_t, valores_v1, valores_v2

# Entradas
def main():

    
    print("t0=0\nv1_0=12\nv2_0=8\n\n")
    print('Digite as condicoes iniciais:')
    t0 = float(input('t0 = '))
    v1_0 = float(input('v1_0 = '))
    v2_0 = float(input('v2_0 = '))

    print('\nPasso: ')
    print("Nesse caso h=0.1")

    h = float(input('h = '))

    print('\nQuantidade de iteracoes:')
    print("n=1000 gera valores suficientes")
    step = int(input('n = '))

    # chamada rk4
    valores_t, valores_v1,valores_v2 = rk4(t0,v2_0,v1_0,h,step)

    # variando x(tempo) de 0 a 40
    plt.xlim(0, 40)

    # variando y(v) de 0 a 20
    plt.ylim(0, 20)

    # plotando grafico de v_2
    plt.plot(valores_t, valores_v2)

    # plotando grafico de v_1
    plt.plot(valores_t, valores_v1)

    # legenda do grafico
    plt.xlabel('t')

    # legenda do grafico
    plt.ylabel('v')

    # titulo do grafico
    plt.title('Estado de escoamento dos tanques')

    plt.grid(True)

    plt.savefig("rk4.png")

    with open("resultados_v1", "w") as file:
            file.write("RESULTADOS V1\n\n")
            for i in range(len(valores_t)):
                file.write("t = %f\tv1 = %f\n" % (valores_t[i], valores_v1[i]))

    with open("resultados_v2", "w") as file:
            file.write("RESULTADOS V2\n\n")
            for i in range(len(valores_t)):
                file.write("t = %f\tv2 = %f\n" % (valores_t[i], valores_v2[i]))

    print("\nGrafico gerado com sucesso!")
    print("Arquivo de resultados escrito com sucesso!")

    
if __name__ == "__main__":
    main()