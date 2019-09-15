
class No():
    def __init__(self, id):
        self.id = id
        self.visitado = False
        self.predecessor = []

    def setVisitado(self, valor):
        self.visitado = valor

    def getVisitado(self):
        return self.visitado

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setEstimativa(self, estimativa):
        self.estimativa = estimativa

    def getEstimativa(self):
        return self.estimativa
    
    def __str__(self):
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
        return (" Cidade  : %s \n Distancia: %i km\n" % (cidades[self.id], self.estimativa))  # imprimir o predecesso

