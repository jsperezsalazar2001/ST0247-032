from GraphAL import *
import math
class Lab4:
    def shortestRoute(g):
        minPath = math.inf
        p = [0] * (g.size + 1)
        for x in range(g.size):
            path = 0
            v = 0
            cont = 0
            index = 0
            min = 0
            valued = [False] * g.size
            for i in range(g.size):
                v = index
                successors = g.getSuccessors(v)
                min = math.inf
                valued[v] = True
                cont += 1
                j = 0
                while (j < len(successors)):
                    costo = g.getWeight(v, successors[j])
                    if min > costo and (valued[successors[j]] == False or (successors[j] == x and cont == g.size)):
                        print(str(valued[successors[j]]) + " " + str(j)+" entra if")
                        min = costo
                        index = successors[j]
                        p[x] = successors[j]
                        print("index: "+str(index)+" v: "+str(v)+" hijos j : "+str(successors[j])+" costo:"+str(costo))

                    j += 1
                if min != math.inf:
                    path += min
            if minPath > path:
                minPath = path
        print(minPath)
        print(p)
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
    shortestRoute(grafo)

