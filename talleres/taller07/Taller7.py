# This file contains methods that use dijkstra and Prim algorithm

from GraphAL import *
from GraphAM import *
import math

class Taller7:


    def fillArrayWithInfinities(self, n, v):
        a = [math.inf]*n
        a[v] = 0
        return a

    def theSmallestNotVisited(self, g, visited, table):
        min = math.inf
        for i in range(g.size):
            if table[i] < min and visited[i] == False:
                min = table[i]

        return min

    def updateWeightsWithCurrentValue(self, g, current, table):
        if table[current] != math.inf :
            successors = g.getSuccessors(current)
            for i in range(len(successors)):
                value = g.getWeight(current, i)
                if current != i and value != math.inf and (value+table[current] < table[i]):
                    table[i] = table[current] + value

    def dijkstra(self, g, v):
        table = self.fillArrayWithInfinities(g.size, v)
        current = v
        visited = [False]*g.size

        for i in range(g.size):
            current = self.theSmallestNotVisited(g, visited, table)
            visited[current] = True
            self.updateWeightsWithCurrentValue(g, current, table)

        return table

    def getMinWeight(self, g, visited, table):
        min = math.inf
        vMin = 0
        father = 0
        for i in range(len(table)):
            successors = g.getSuccessors(table[i])
            for j in range(len(successors)):
                value = g.getWeight(table[i], successors[j])
                if value < min and visited[successors[j]] == False:
                    min = value
                    vMin = successors[j]
                    father = table[i]
        return [father, vMin]

    def prim(self, g, v):
        father = [None]*g.size
        table = [v]
        visited = [False]*g.size
        visited[v] = True
        father[v] = v
        current = v

        for i in range(g.size-1):
            tup = self.getMinWeight(g, visited, table)
            current = tup[1]
            visited[current] = True
            father[current] = tup[0]
            table.append(current)

        tree = []
        pathCost= 0
        for k in range(len(table)):
            tree.append([table[k], father[table[k]]])
            if k != 0:
                pathCost += g.getWeight(table[k], father[table[k]])

        return str(tree) + " path cost: " + str(pathCost)


graph = GraphAl(5)
graph.addArc(0, 1, 2)
graph.addArc(0, 2, 2)
graph.addArc(0, 3, 1)
graph.addArc(0, 4, 4)
graph.addArc(1, 0, 2)
graph.addArc(1, 2, 3)
graph.addArc(1, 3, 2)
graph.addArc(1, 4, 3)
graph.addArc(2, 0, 2)
graph.addArc(2, 1, 3)
graph.addArc(2, 3, 2)
graph.addArc(2, 4, 2)
graph.addArc(3, 0, 1)
graph.addArc(3, 1, 2)
graph.addArc(3, 2, 2)
graph.addArc(3, 4, 4)
graph.addArc(4, 0, 4)
graph.addArc(4, 1, 3)
graph.addArc(4, 2, 2)
graph.addArc(4, 3, 4)

graph2 = GraphAl(6)
graph2.addArc(0, 1, 9)
graph2.addArc(0, 2, 1)
graph2.addArc(0, 3, 8)
graph2.addArc(1, 0, 9)
graph2.addArc(1, 2, 2)
graph2.addArc(1, 4, 3)
graph2.addArc(2, 0, 1)
graph2.addArc(2, 1, 2)
graph2.addArc(2, 3, 6)
graph2.addArc(2, 4, 4)
graph2.addArc(3, 0, 8)
graph2.addArc(3, 2, 6)
graph2.addArc(3, 5, 7)
graph2.addArc(4, 1, 3)
graph2.addArc(4, 2, 4)
graph2.addArc(4, 5, 5)
graph2.addArc(5, 4, 5)
graph2.addArc(5, 3, 7)

taller7 = Taller7()
# print(taller7.dijkstra(graph, 0))
print(taller7.prim(graph2, 0))


