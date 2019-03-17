class GraphAm:
    matriz = []
    size = 0

    def __init__(self, size):

        self.size = size
        for i in range(size):
            self.matriz.append([-1]*size)

    def getEdges(self):
        return self.matriz

    def getWeight(self, source, destination):
        return self.matriz[source][destination]

    def addArc(self, source, destination, weight):
        self.matriz[source][destination]=weight

    def getSuccessors(self, vertex):
        lista = []
        for i in range(self.size):
            if(self.matriz[vertex][i] != -1):
                lista.append(i)

        return lista

    def __str__(self):
        for i in self.matriz:
            print(i)
