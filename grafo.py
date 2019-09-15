from no import No
from aresta import Aresta

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
        lista = self.busca_todas_arestas(u)
        print (len(lista))
        for l in lista:
            if l.getVisitado() is False:
                l.setVisitado(True)
                print("Visitando o no: %s" % l.getId())
        for m in lista:
            lista2 = self.busca_todas_arestas(m)
            for n in lista2:
                if n.getVisitado() is False:
                    self.visita(m)
            

    def DFS(self,u):

        for v in self.lista_nos:
            v.setVisitado(False)
        no_0 = self.busca_no(u)

        print("Visitando o no: %s" % no_0.getId())

        self.visita(no_0)

    # Fim busca em profundidade 

    ## Dijkstra
    def inicializa_fonte(self, fonte):
        for v in self.lista_nos:
            v.setEstimativa(99999)
            v.setVisitado(False)
        fonte.setVisitado(True)
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
                return destino
        else:
            return None

    def compara_no(self, u, v, w):
        if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
            v.setEstimativa(u.getEstimativa() + w.getPeso())
            v.predecessor.append(u.getId())
