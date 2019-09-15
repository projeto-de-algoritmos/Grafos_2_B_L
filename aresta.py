#Aresta
class Aresta():
	def __init__(self,origem,destino,peso):
		self.origem = origem
		self.destino = destino
		self.peso = peso

	def getOrigem(self):
		return self.origem
		
	def getDestino(self):
		return self.destino
	
	def getPeso(self):
		return self.peso
		
	def setOrigem(self,vertice):
		self.origem = vertice
		
	def setDestino(self,vertice):
		self.destino = vertice
	
	def printAresta(self):
		print("%s ------ %s ------> %s" % self.origem, self.destino, self.peso)