from grafo import Grafo
import time
import pygame

try:
    pygame.init()

except:
    print("nao foi iniciado com sucesso")

largura, altura = 700,500
pygame.display.set_mode((largura,altura))


g = Grafo()
for i in range(0,12):
    g.new_no(i)

g.nova_aresta(1,2,22)
g.nova_aresta(1,0,15)
g.nova_aresta(2,3,32)
g.nova_aresta(2,4,19)
g.nova_aresta(2,5,20)
g.nova_aresta(3,5,18)
g.nova_aresta(4,8,23)
g.nova_aresta(4,7,20)
g.nova_aresta(5,8,19)
g.nova_aresta(5,7,10)
g.nova_aresta(5,6,21)
g.nova_aresta(8,0,11)
g.nova_aresta(8,11,11)
g.nova_aresta(7,11,24)
g.nova_aresta(7,10,28)
g.nova_aresta(6,10,23)
g.nova_aresta(6,9,23)

n = 0

inicio = time.time()
g.prim(1)

g.display()
