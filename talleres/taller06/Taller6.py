from GraphAM import *
from GraphAL import *
import math


class Taller6:

    def cambioGreedy (n, denominaciones):
        denominaciones.sort(reverse=True)
        cont = 0
        cantidades = []

        while cont < len(denominaciones):
            cantidad = n//denominaciones[cont]
            cantidades.insert(cont, cantidad)
            n = n % denominaciones[cont]
            cont += 1

        print(cantidades)

    def costoMinimo(g):
        minPath = math.inf
        for x in range(g.size):
            camino = 0
            v = 0
            cont = 0
            index = 0
            min = 0
            valued = [False] * g.size
            for i in range(g.size):
                v = index
                hijos = g.getSuccessors(v)
                min = math.inf
                valued[v] = True
                cont += 1
                j = 0

                while(j < len(hijos)):
                    costo = g.getWeight(v, hijos[j])
                    #print(str(valued[hijos[j]])+str(j))
                    #print(hijos)
                    if min > costo and (valued[hijos[j]] == False or (hijos[j] == x and cont == g.size)):
                        #print(str(valued[hijos[j]]) + " " + str(j)+" entra if")
                        min = costo
                        index = hijos[j]
                        #print("index: "+str(index)+" v: "+str(v)+" hijos j : "+str(hijos[j])+" costo:"+str(costo))
                    j += 1

                if min != math.inf:
                    camino += min
                    
            if minPath > camino:
                minPath = camino
        print(minPath)

    cambioGreedy(900, [1000, 500, 200, 50])
    grafo = GraphAl(5)
    grafo.addArc(0, 1, 2)
    grafo.addArc(0, 2, 2)
    grafo.addArc(0, 3, 1)
    grafo.addArc(0, 4, 4)
    grafo.addArc(1, 0, 2)
    grafo.addArc(1, 2, 3)
    grafo.addArc(1, 3, 2)
    grafo.addArc(1, 4, 3)
    grafo.addArc(2, 0, 2)
    grafo.addArc(2, 1, 3)
    grafo.addArc(2, 3, 2)
    grafo.addArc(2, 4, 2)
    grafo.addArc(3, 0, 1)
    grafo.addArc(3, 1, 2)
    grafo.addArc(3, 2, 2)
    grafo.addArc(3, 4, 4)
    grafo.addArc(4, 0, 4)
    grafo.addArc(4, 1, 3)
    grafo.addArc(4, 2, 2)
    grafo.addArc(4, 3, 4)
    costoMinimo(grafo)

