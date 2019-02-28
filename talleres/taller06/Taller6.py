from GraphAM import *
from GraphAL import *

class Taller6:
    def cambioGreedy(n, denominaciones):
        denominaciones.sort(reverse=True)
        cont=0
        cantidades=[]

        while(cont<len(denominaciones)):
            cantidad = n/denominaciones[cont]
            cantidades.insert(cont, cantidad)
            n = n % denominaciones[cont]
            cont += 1

        print(cantidades)

    def costoMinimo(g, inicio):
        valued = [False]*g.size
        for inicio in g.size:
            hijos = g.getSuccessors(inicio)
            j=1
            for j in len(hijos):
                min = g.getWeight(inicio, hijos[j])
                if min > hijos[j]:
                    min = hijos[j]






    cambioGreedy(900, [1000,500,200,50])
    costoMinimo(GraphAm(5), 0)
