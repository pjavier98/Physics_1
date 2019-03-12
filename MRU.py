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

if(posicao_final < posicao_inicial):#Caso específico da velocidade ter sido digitada positiva quando deveria ser negativa
     velocidade = -abs(velocidade)


fig = plt.figure('MRU')

ax = fig.add_subplot(111) # o numero 111 define o tamanho na interface
ax.grid(True, color = '0.75') # define a cor das linhas dos eixos das coordenadas
ax.set_xlim([-abs(posicao_inicial) - 10, abs(posicao_final) + 10]) # amplia um intervalo dado no x
ax.set_ylim([0, ((posicao_final-posicao_inicial) / velocidade) + 10]) # amplia um intervalo dado no x

scat = plt.scatter(posicao_inicial, 0)
scat.set_alpha(0.5) # seta a cor da bola

# frames: distancia que ele vai percorrer
# interval: velocidade
lista = []
x = posicao_inicial
y = 0
if(posicao_final == -posicao_inicial):
     aux = 2 * abs(posicao_final) * 10
else:
    aux = abs(int((posicao_final - posicao_inicial) / velocidade)) * 10
print(aux)
for i in range(aux):# *10 pra rodar o loop mais vezes e diminuir o tamanho so salto da bola
     x += velocidade / 10
     y += 0.1
     lista.append([x, y])
     
anim = animation.FuncAnimation(fig, _update_plot, fargs = (fig, scat), frames = lista, interval = 60)

plt.show()
