from matplotlib import pyplot as plt
import matplotlib.animation as animation
from math import sqrt
import numpy as np


def _update_plot(i, fig, scat):
    scat.set_offsets(([i, i]))
    return scat


print("Insira a posição inicial: ")
posicao_inicial = float(input())
print("Insira a posição final: ")
posicao_final = float(input())
print("Insira a velocidade: ")
velocidade = float(input())
x = 0
y = posicao_inicial
lista = []

fig = plt.figure('MRU')

ax = fig.add_subplot(111)  # o numero 111 define o tamanho na interface
# define a cor das linhas dos eixos das coordenadas
ax.grid(True, color='0.75')
ax.set_ylim([-max(abs(posicao_inicial), abs(posicao_final)) * 15 / 10, max(abs(posicao_inicial), abs(posicao_final)) * 15 / 10])  # amplia um intervalo dado no x
ax.set_xlabel('Time')
ax.set_ylabel('Space')

scat = plt.scatter(posicao_inicial, 0)
scat.set_alpha(0.5)  # define a cor da bola

if(velocidade != 0):
     # Caso específico da velocidade ter sido digitada positiva quando deveria ser negativa
     if(posicao_final < posicao_inicial):
          velocidade = -abs(velocidade)
     if(posicao_final == -posicao_inicial):  # Ex: quando for 500 e -500
          aux = abs(int((2 * posicao_final / velocidade))) * 10
     else:
          aux = abs(float((abs(posicao_final) + abs(posicao_inicial)) / velocidade)) * 10
     if(aux != int(aux)):
          aux = int(aux) + 1
     print(aux)
     for i in range(int(aux)):  # *10 pra rodar o loop mais vezes e diminuir o tamanho so salto da bola
          x += 0.1
          y += velocidade / 10
          lista.append([x, y])
     # amplia um intervalo dado no x
     ax.set_xlim([-1, ((posicao_final - posicao_inicial) / velocidade) + 10])
else:
     ax.set_xlim([-1, 10])  # amplia um intervalo dado no y

# frames: distancia que ele vai percorrer
# interval: velocidade
anim = animation.FuncAnimation(fig, _update_plot, fargs=(fig, scat), frames=lista, interval=60)
plt.show()
