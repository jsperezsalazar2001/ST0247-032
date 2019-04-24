from Graph import *
from Arc import *
from Node import *
import math


class OrderFinder:

    def __init__(self):
        self.__distancesArray = []

    def getTargetDistance(self, graph):
        for i in range(len(graph)):
            self.__distancesArray.append(graph[i][0])
        self.__distancesArray.sort(key=lambda x: x.getDistance(), reverse=True)
        return self.__distancesArray

    def orderFinder(self, distancesArray, graph, p):
        if len(distancesArray) <= 20:
            #for j in distancesArray:
                #if j.getNodeFrom() is not None:
                    #print(j.getNodeFrom().getID())
            for i in distancesArray:
                iniNode = i.getNodeFrom()
                print(iniNode)
                if (iniNode is not None) and (iniNode.getPickedUp() is False):
                    print("ya")
                    iniNode.addPassenger(iniNode)
                    iniNode.setPickedUp(True)
                    cont = 1
                    successorsNumber = 0
                    maxTimesToTarget = [int(graph[iniNode.getID()-1][0].getTime())*p]
                    lastPickedUp = iniNode
                    successors = self.getDistanceFromToSorted(graph, iniNode)
                    while cont <= 5 and successorsNumber < len(successors):
                        successors = self.getDistanceFromToSorted(graph, lastPickedUp)
                        nodeTo = successors[successorsNumber].getNodeTo()
                        canPickUp = True
                        if nodeTo is not None and nodeTo.getPickedUp() is False:
                            for maxTime in maxTimesToTarget:
                                if (maxTime - graph[lastPickedUp.getID()-1][nodeTo.getID()-1] - graph[nodeTo.getID()-1][0]) <= 0:
                                    canPickUp = False
                            if canPickUp:
                                iniNode.addPassenger(nodeTo)
                                for max in range(len(maxTimesToTarget)):
                                    maxTimesToTarget[max] -= graph[lastPickedUp.getID()-1][nodeTo.getID()-1].getTime()
                                maxTimesToTarget.append(graph[nodeTo.getID()-1][0].getTime())
                                lastPickedUp = nodeTo
                                nodeTo.setPickedUp(True)
                                # nodeTo.setPickedUpBy(self, lastPickedUp)
                                cont += 1
                                successorsNumber = 0
                            else:
                                successorsNumber += 1


        #initialPickers = len(distancesArray)/5
        #answer = [len(distancesArray)]
        #for i in range(initialPickers):

    def showAnswer(self):
        for arc in self.__distancesArray:
            node = arc.getNodeFrom()
            if node is not None: #and len(node.getPassengers()) != 0:
                print ("hpta")
                print(node.getPassengers())

    def getDistanceFromToSorted(self, graph, node1):
        sortedArray = []
        for i in range(len(graph)):
            sortedArray.append(graph[node1.getID()][i])
        sortedArray.sort(key=lambda x: int(x.getTime()))
        return sortedArray


