from tkinter import *
import math
import time

master = Tk()
w = Canvas(master, width=768, height=768)
w.pack()

w.create_line(384, 768, 384, 0)
w.create_line(0, 384, 768, 384)
for i in range(16,768,16):
	w.create_line(i,380,i,388)
for i in range(16,768,16):
	w.create_line(380,i,388,i)
print("Digite o raio:")
r = int(input())
r *= 16
print("Digite as coordenadas x e y do centro da circunferência:")
x,y = list(map(int, input().split()))
x *= 16
y *= 16
ball = w.create_oval(x+382+r, 382-y, x+386+r, 386-y, fill = "red")

C_x = x + 384
C_y = y + 384

x += 384 + r
y = 384 - y
aux_x = x
aux_y = y

print(aux_x,aux_y)

while(aux_x > C_x):
	aux_x -= 0.8
	aux_y = math.sqrt(pow(r+384,2) - pow(aux_x,2))
	print(aux_x,aux_y)
	# w.move(ball, -0.8, -0.8)
	# master.update()
	# time.sleep(0.01)
mainloop()


# for i in range(370):
# 	w.move(ball, 1, -1)
# 	master.update()
# 	time.sleep(0.01)
