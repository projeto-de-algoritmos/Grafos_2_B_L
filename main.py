from grafo import Grafo
import time

g2 = Grafo()
for i in range(0,9):
    g2.new_no(i)

g2.nova_aresta(1,3,232)
g2.nova_aresta(1,2,32)
g2.nova_aresta(3,4,345)
g2.nova_aresta(2,4,324)
g2.nova_aresta(4,5,23)
g2.nova_aresta(5,6,23)
g2.nova_aresta(5,7,44)
g2.nova_aresta(6,7,23)
g2.nova_aresta(7,0,24)
g2.nova_aresta(0,4,24)
g2.nova_aresta(0,3,24)

n = 0

inicio = time.time()
g2.prim(1)

cidades ={ 0 : "Gama",
            1 : "Ceilandia",
            2 : "Taguatinga",
            3 : "Guara",
            4 : "Aguas Lindas",
            5 : "Riacho Fundo",
            6 : "Aguas Claras",
            7 : "P SUl",
            8 : "Samanbaia",
            9 : "Brasilia",
            10 : "M Norte"}

