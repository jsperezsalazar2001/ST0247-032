from Graph import *
from Arc import *
from Node import *
import math


class OrderFinder:

    def __init__(self):
        self.__distancesArray = []

    def getTargetDistance(self, graph):
        for i in range(len(graph) - 1):
            self.__distancesArray.append(graph[i+1][0])
        self.__distancesArray.sort(key=lambda x: x.getDistance(), reverse=True)
        return self.__distancesArray

    def orderFinder(self, distancesArray, graph, p, mode):
        graph[0][0].getNodeFrom().setPickedUp(True)
        if len(distancesArray) <= 206:
            for i in distancesArray:
                iniNode = i.getNodeFrom()
                #print(iniNode)
                if (iniNode is not None) and (iniNode.getPickedUp() is False):
                    #print("ya")
                    iniNode.addPassenger(iniNode)
                    iniNode.setPickedUp(True)
                    cont = 1
                    successorsNumber = 0
                    if mode == 0:
                        maxTimesToTarget = [int(graph[iniNode.getID()-1][0].getTime())*p]
                    elif mode == 1:
                        maxTimesToTarget = [int(graph[iniNode.getID() - 1][0].getTime()) + p]
                    #print("Max time to target:")
                    #print(maxTimesToTarget)
                    lastPickedUp = iniNode
                    successors = self.getDistanceFromToSorted(graph, iniNode)
                    while cont < 5 and successorsNumber < len(successors):
                        #print("cont: "+str(cont)+" sn: "+str(successorsNumber))
                        #print(lastPickedUp)
                        successors = self.getDistanceFromToSorted(graph, lastPickedUp)
                        nodeTo = successors[successorsNumber].getNodeTo()
                        #print("Successors: ")
                        #self.imprimirArrayArcos(successors)
                        #print("Node from: " + str(successors[successorsNumber].getNodeFrom().getID())+ " Node to: "+str(nodeTo.getID())+" / Nodeto is pickedUP?: " + str(nodeTo.getPickedUp()))
                        canPickUp = True
                        if nodeTo is not None and nodeTo.getPickedUp() is not True:
                            #print("Entra if 1")
                            for maxTime in maxTimesToTarget:
                                if (maxTime - graph[lastPickedUp.getID()-1][nodeTo.getID()-1].getTime() - graph[nodeTo.getID()-1][0].getTime()) <= 0:
                                    #print("entra if 2")
                                    #print("LastPickedUp"+str(lastPickedUp.getID()))
                                    canPickUp = False
                                    break

                            if canPickUp:
                                iniNode.addPassenger(nodeTo)
                                for max in range(len(maxTimesToTarget)):
                                    maxTimesToTarget[max] -= graph[lastPickedUp.getID()-1][nodeTo.getID()-1].getTime()
                                if mode == 0:
                                    maxTimesToTarget.append(int(graph[nodeTo.getID() - 1][0].getTime()) * p)
                                elif mode == 1:
                                    maxTimesToTarget.append(int(graph[nodeTo.getID() - 1][0].getTime()) + p)
                                #print(maxTimesToTarget)
                                lastPickedUp = nodeTo
                                nodeTo.setPickedUp(True)
                                # nodeTo.setPickedUpBy(self, lastPickedUp)
                                cont += 1
                                successorsNumber = 0
                            else:
                                successorsNumber += 1
                        else:
                            successorsNumber += 1

        #initialPickers = len(distancesArray)/5
        #answer = [len(distancesArray)]
        #for i in range(initialPickers):

    def showAnswer(self, numberOfCars, p):
        filename = "./answers/resultCarpoolingRouting-U_"+str(numberOfCars)+"-p_"+str(p)+".txt"
        result = open(filename, "w+")
        cont = 0
        for arc in self.__distancesArray:
            node = arc.getNodeFrom()
            if node is not None and len(node.getPassengers()) != 0:
                cont += 1
                nodes = (node.getPassengers())
                contNodes = 0
                result.write("[ ")
                for n in nodes:
                    contNodes += 1
                    if contNodes < len(nodes):
                        result.write(str(n.getID()) + ", ")
                    else:
                        result.write(str(n.getID()))
                result.write(" ]\n")
        result.write("Number of cars: " + str(cont))

    def getDistanceFromToSorted(self, graph, node1):

        sortedArray = []
        for i in range(len(graph)):
            if i != int(node1.getID() - 1):
                sortedArray.append(graph[int(node1.getID()) - 1][i])
        sortedArray.sort(key=lambda x: int(x.getTime()))
        #print(sortedArray)
        return sortedArray

    def imprimirArrayArcos(self, arr):
        print("[", end="")
        for i in range(len(arr) - 1):
            print(arr[i].getNodeTo().getID(), end=",")
        print(arr[len(arr) - 1].getNodeTo().getID(), end="")
        print("]")
