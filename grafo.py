from no import No
from aresta import Aresta
import pygame


class Grafo:
    def __init__(self):
        self.lista_nos = []
        self.lista_arestas = []

    def new_no(self, id_nome): #cria no
        novo_no = No(id_nome)
        self.lista_nos.append(novo_no)
   
    def busca_aresta(self, u, v):  # Metodo recebe dois nos e retorna a aresta que liga os dois
        for w in self.lista_arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w

    def busca_no(self, identificador):
        #print(self.lista_nos)
        for i in self.lista_nos:
            if identificador == i.getId():
                return i
        else:
            print("No nao encontrado")
            return None

    def nova_aresta(self, origem, destino, peso):
        origem_aux = self.busca_no(origem)
        destino_aux = self.busca_no(destino)
        '''
        if (origem_aux):
            #print(origem)      
        if (destino_aux):
            print(destino)      
        '''
        if ((origem_aux is not None) and (destino_aux is not None)):
            self.lista_arestas.append(Aresta(origem_aux, destino_aux, peso))
            #print("aresta criada")
        else:
            print("############  ERROR  ############")
            print("Aresta nao criada nos invalidos")

    def busca_todas_arestas(self, u):
        nos_conectados = []
        for w in self.lista_arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() :
                nos_conectados.append(destino)

        return nos_conectados

    # busca em profundidade

    def visita(self, u):
        u.setVisitado(True)
        u.setColor(2)
        lista = self.busca_todas_arestas(u)
        #print (len(lista))
        for l in lista:
            if l.getVisitado() is False:
                l.setVisitado(True)
                l.setColor(2)

                print("Visitando o no: %s" % l.getId())
        for m in lista:
            lista2 = self.busca_todas_arestas(m)
            for n in lista2:
                if n.getVisitado() is False:
                    self.visita(m)
            

    def DFS(self,u):

        for v in self.lista_nos:
            v.setVisitado(False)
            v.setColor(1)

        no_0 = self.busca_no(u)

        print("Visitando o no: %s" % no_0.getId())

        self.visita(no_0)

    # Fim busca em profundidade 

    ## Dijkstra
    def inicializa_fonte(self, fonte):
        for v in self.lista_nos:
            v.setEstimativa(9999999999)
            v.setVisitado(False)
            v.setColor(1)
        fonte.setVisitado(True)
        fonte.setColor(2)

        fonte.setEstimativa(0)

    def busca_vertice(self, identificador):
        for i in self.lista_nos:
            if identificador == i.getId():
                return i
        else:
            return None

    def busca_adjacente(self, u):  
        for i in range(len(self.lista_arestas)):
            origem = self.lista_arestas[i].getOrigem()
            destino = self.lista_arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getVisitado() == False):
                destino.setVisitado(True)
                destino.setColor(2)

                return destino
        else:
            return None

    def compara_no(self, u, v, w):
        if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
            v.setEstimativa(u.getEstimativa() + w.getPeso())
            v.predecessor.append(u.getId())

    def dijkstra(self, origem):
        fonte = self.busca_vertice(origem)
        if fonte is None:
            return "Vertce Nulo"

        self.inicializa_fonte(fonte)
        lista = []
        resposta = []  
        for i in self.lista_nos:
            lista.append(i)
        while len(lista) != 0:
            lista.sort()
            u = lista[0]
            v = self.busca_adjacente(u)
            if v is None:
                for i in self.lista_nos:
                    i.setVisitado(False)
                    i.setColor(1)
                resposta.append(lista[0])
                lista.pop(0)  # retira vertice sem adjacente da lista


            else:
                w = self.busca_aresta(u, v)
                if w is not None:
                    self.compara_no(u, v, w)

        print("Estimativas: ")
        for i in resposta:
            print(i)  # imprime as respostas

    #Implementacao do algoritimo de PRIM
    def prim(self, origem):
        
        fonte = self.busca_no(origem)
        
        if fonte is None:
            return "Vertice Nulo"

        self.inicializa_fonte(fonte)
        lista = []
        for i in self.lista_nos:
            lista.append(i)
        lista.sort()
        while len(lista) is not 0:
            u = lista[0]
            v = self.busca_adjacente(u)

            if v is None:
                for i in lista:  # prepara para ser visitado
                    i.setVisitado(False)  # marca como n visitado
                    i.setColor(1)                    
                lista.sort()
                lista.remove(u)
            else:
                w = self.busca_aresta(u, v)
                if lista.count(v) > 0:
                    if v.getEstimativa() > w.getPeso():
                        v.predecessor = [u.getId()]
                        v.setEstimativa(w.getPeso())
        
        print ("\nAlgoritmo de PRIM:\n")

        for u in self.lista_nos:
            if len(u.predecessor) > 0:
                var = str(u.predecessor[0])
                var2 = str(u.getId())
                print("R" + var + " ------  " + "R" +  var2)
        self.lista_nos.sort(key=lambda u: u.input, reverse=False)
        for i in self.lista_nos:
            print(i)

        print("\n\n")


    #implementacao da interface        
    def display(self):
        pygame.init()
        screen = pygame.display.set_mode((500, 500))
        done = False
        color_pack = True
        x = 30
        y = 30

        clock = pygame.time.Clock()

        color_line=[]

        while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            color_pack = not color_pack
                
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: y -= 3
            if pressed[pygame.K_DOWN]: y += 3
            if pressed[pygame.K_LEFT]: x -= 3
            if pressed[pygame.K_RIGHT]: x += 3
                
            screen.fill((0, 0, 0))


            if color_pack: 
                        color = (0, 255, 0)
            else: 
                    self.dijktra(1)
            x = 150
            y = 100
            for i in self.lista_nos:
                if i.getColor() is 1:
                        color_line.append((0, 255, 0))
                else:
                        color_line.append((255, 100, 0))

            pygame.draw.circle(screen, color_line[3], (x+40, y), 5, 5)
            pygame.draw.circle(screen, color_line[2], (x, y), 5, 5)
            pygame.draw.circle(screen, color_line[1], (x-40, y), 5, 5)
            pygame.draw.circle(screen, color_line[5], (x+30, y+40), 5, 5)
            pygame.draw.circle(screen, color_line[4], (x-30, y+40), 5, 5)
            pygame.draw.circle(screen, color_line[8], (x-50, y+80), 5, 5)
            pygame.draw.circle(screen, color_line[6], (x+50, y+80), 5, 5)
            pygame.draw.circle(screen, color_line[7], (x, y+80), 5, 5)
            pygame.draw.circle(screen, color_line[9], (x+70, y+120), 5, 5)
            pygame.draw.circle(screen, color_line[0], (x-70, y+120), 5, 5)
            pygame.draw.circle(screen, color_line[10], (x+25, y+120), 5, 5)
            pygame.draw.circle(screen, color_line[11], (x-25, y+120), 5, 5)
            

            pygame.draw.line(screen, color, [x,y],[x+30,y+40],1)
            pygame.draw.line(screen, color, [x+40, y],[x+30,y+40],1)
            pygame.draw.line(screen, color, [x,y],[x+40, y],1)
            pygame.draw.line(screen, color, [x-40, y],[x, y],1)
            pygame.draw.line(screen, color, [x, y],[x-30, y+40],1)
            
            pygame.draw.line(screen, color, [x-30, y+40],[x-50, y+80],1)
            pygame.draw.line(screen, color, [x-30, y+40],[x, y+80],1)

            pygame.draw.line(screen, color, [x+30, y+40],[x-50, y+80],1)
            pygame.draw.line(screen, color, [x+30, y+40],[x, y+80],1)
            pygame.draw.line(screen, color, [x+30, y+40],[x+50, y+80],1)

            pygame.draw.line(screen, color, [x+50, y+80],[x+70, y+120],1)
            pygame.draw.line(screen, color, [x+50, y+80],[x+25, y+120],1)
            pygame.draw.line(screen, color, [x, y+80],[x+25, y+120],1)
            pygame.draw.line(screen, color, [x, y+80],[x-25, y+120],1)
            pygame.draw.line(screen, color, [x-50, y+80],[x-70, y+120],1)

            pygame.draw.line(screen, color, [x-40, y],[x-70, y+120],1)

            pygame.display.flip()
            clock.tick(60)


