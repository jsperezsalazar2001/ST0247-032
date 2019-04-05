from Graph import *
from Arc import *
from Node import *
import math

class OrderFinder:

    __distancesArray = []

    def __init__(self):
        __distancesArray = []

    def getTargetDistance(self, graph):
        for i in range(len(graph)):
            self.__distancesArray.append(graph[0][i])
        self.__distancesArray.sort(key=lambda x: x.getDistance(), reverse=True)
        return self.__distancesArray

    def orderFinder(self, distancesArray):
        initialPickers = len(distancesArray)/5
        answer = [len(distancesArray)]
        #for i in range(initialPickers):

    def getDistanceFromToSorted(self, graph, node1):
        sortedArray = []
        for i in range(len(graph)):
            sortedArray.append(graph[node1][i])
        sortedArray.sort(key=lambda x: x.getTime())
        return sortedArray


prueba = Graph()
prueba.readGraph("dataset-ejemplo-U=4-p=1.2.txt", 4)
order = OrderFinder()
print(order.getTargetDistance(prueba.getMatrix()))