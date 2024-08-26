import numpy as np
import matplotlib.pyplot as plt

# Função para equação de primeiro grau
def linha(x, a, b):
    return a * x + b

# Função para equação de segundo grau
def parabola(x, a, b, c):
    return a * x**2 + b * x + c

# Definindo os coeficientes para as equações
a1, b1 = 2, -3  # Coeficientes para a equação de primeiro grau
a2, b2, c2 = 1, -2, -3  # Coeficientes para a equação de segundo grau

# Gerando um intervalo de valores para x
x = np.linspace(-10, 10, 400)

# Calculando os valores de y para cada equação
y1 = linha(x, a1, b1)
y2 = parabola(x, a2, b2, c2)

# Criando o gráfico
plt.figure(figsize=(12, 6))

# Gráfico para a equação de primeiro grau
plt.subplot(1, 2, 1)
plt.plot(x, y1, label=f'y = {a1}x + {b1}', color='blue')
plt.title('Equação de Primeiro Grau')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()

# Gráfico para a equação de segundo grau
plt.subplot(1, 2, 2)
plt.plot(x, y2, label=f'y = {a2}x^2 + {b2}x + {c2}', color='red')
plt.title('Equação de Segundo Grau')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()

# Ajuste do layout e exibição do gráfico
plt.tight_layout()
plt.show()
