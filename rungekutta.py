import matplotlib.pyplot as plt
import numpy as np
# RK-4 python
# EDO
def v2(t,v2):
    return -v2/4 + 1

def v1(t,v2,v1):
    return -(v1/4) + v2/4 + 1

def h1(t, v1, v2):
    return -(v1*t)/4 + (v2*t)/4 + t + 2.009608 + 0.183051       # essa soma é a altura inicial do tanque 1

def h2(t, v2):
    return -(v2*t)/4 + t + 1.055626 + 0.415892                  # essa soma é a altura inicial do tanque 2

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

    plt.figure()
    # variando x(tempo) de 0 a 40
    plt.xlim(0, 80)

    # variando y(v) de 0 a 20
    plt.ylim(0, 20)

    # plotando grafico de v_2
    plt.plot(valores_t, valores_v2)

    # plotando grafico de v_1
    plt.plot(valores_t, valores_v1)

    # legenda do grafico
    plt.xlabel('Tempo')

    # legenda do grafico
    plt.ylabel('Velocidade')

    # titulo do grafico
    plt.title('Estado de escoamento dos tanques')

    plt.grid(True)

    plt.savefig("rk4.png")

    plt.close()

    valores_h1 = []
    valores_h2 = []


    with open("altura_tanque_2.txt", "w") as file:
        file.write("ALTURA TANQUE 2\n\n")
        for i in range(len(valores_t)):
            file.write("t = %f\th2 = %f\n" % (valores_t[i], h2(valores_t[i], valores_v2[i])))
            valores_h2.append(h2(valores_t[i], valores_v2[i]))

    with open("altura_tanque_1.txt", "w") as file:
        file.write("ALTURA TANQUE 1\n\n")   
        for i in range(len(valores_t)):
            file.write("t = %f\th1 = %f\n" % (valores_t[i], h1(valores_t[i], valores_v1[i], valores_v2[i])))
            valores_h1.append(h1(valores_t[i], valores_v1[i], valores_v2[i]))

    with open("resultados_v1", "w") as file:
            file.write("RESULTADOS V1\n\n")
            for i in range(len(valores_t)):
                file.write("t = %f\tv1 = %f\n" % (valores_t[i], valores_v1[i]))

    with open("resultados_v2", "w") as file:
            file.write("RESULTADOS V2\n\n")
            for i in range(len(valores_t)):
                file.write("t = %f\tv2 = %f\n" % (valores_t[i], valores_v2[i]))


    plt.figure()

    plt.xlim(0, 80)

    plt.plot(valores_t, valores_h1)

    plt.xlabel('Tempo')

    plt.ylabel('Altura')

    plt.title('Altura do tanque 1')

    plt.savefig("altura_tanque_1.png")

    plt.close()

    plt.figure()

    plt.xlim(0, 80)

    plt.plot(valores_t, valores_h2)

    plt.xlabel('Tempo')

    plt.ylabel('Altura')

    plt.title('Altura do tanque 2')

    plt.savefig("altura_tanque_2.png")

    plt.close()

    print("\nGraficos gerados com sucesso!")
    print("Arquivo de resultados escrito com sucesso!")

    
if __name__ == "__main__":
    main()