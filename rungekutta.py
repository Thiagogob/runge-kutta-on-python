import matplotlib as plt
import numpy as np
plt.use('agg')

def runge_kutta(f, x0, y0, h, n):
    """
    Implementação do método de Runge-Kutta de quarta ordem.

    Args:
        f: Função que define a equação diferencial dy/dx = f(x, y).
        x0: Valor inicial de x.
        y0: Valor inicial de y.
        h: Tamanho do passo.
        n: Número de passos a serem executados.

    Returns:
        Duas listas: a primeira contém os valores de x, e a segunda contém os valores de y.
    """
    valores_x = [x0]
    valores_y = [y0]

    for i in range(n):
        x = valores_x[-1]
        y = valores_y[-1]

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        x_prox = x + h
        y_prox = y + (k1 + 2*k2 + 2*k3 + k4) / 6

        valores_x.append(x_prox)
        valores_y.append(y_prox)

    return valores_x, valores_y

def f(v, t):
    return -(v/4) + 1

t0 = 0
v0 = 8
h = 0.1
n = 10

valores_x, valores_y = runge_kutta(f, t0, v0, h, n)

for x, y in zip(valores_x, valores_y):
    print(f"x = {x}, y = {y}")


if __name__ == "__f__":
    f()