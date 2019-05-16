from Graph import *
import math


class OrderFinder:
    """
    This class contains the main algorithm which finds the sets of cars
    :author Juan Sebastian Perez Salazar
    :author Yhoan Alejandro Guzman Garcia
    """

    def __init__(self):
        """
        Class constructor
        """
        self.__distancesArray = []
        self.__answerMatrix = [[]]
        self.__totalNumberOfCars = 0
    def getTargetDistance(self, graph):
        """
        This method calculates the distance between a Node and target Node in descended order
        :param graph: The matrix of Arcs
        :return: an ordered array of distances in time
        """
        for i in range(len(graph) - 1):
            self.__distancesArray.append(graph[i+1][0])

        self.__distancesArray.sort(key=lambda x: x.getDistance(), reverse=True)
        return self.__distancesArray

    def orderFinder(self, distancesArray, graph, p, mode):
        """
        This method finds the sets of cars
        :param distancesArray: an ordered array by distances in time
        :param graph: the matrix of Arcs
        :param p: time or percentage that every Node can be delayed
        :param mode: the extra time has two modes, minutes and a percentage time
        :return: None
        """
        
        graph[0][0].getNodeFrom().setPickedUp(True)

        for i in distancesArray:
            

            iniNode = i.getNodeFrom()

            if (iniNode is not None) and (iniNode.getPickedUp() is False):
                iniNode.addPassenger(iniNode)
                iniNode.setPickedUp(True)
                cont = 1
                successorsNumber = 0

                if mode == 0:
                    maxTimesToTarget = [int(graph[iniNode.getID() - 1][0].getTime()) * p]
                    minimum = int(graph[iniNode.getID() - 1][0].getTime()) * p
                elif mode == 1:
                    maxTimesToTarget = [int(graph[iniNode.getID() - 1][0].getTime()) + p]
                    minimum = int(graph[iniNode.getID() - 1][0].getTime()) + p

                lastPickedUp = iniNode
                lastCont = -1
                
                while cont < 5 and successorsNumber < len(distancesArray):

                    if lastCont != cont:
                        successors = self.getDistanceFromToSorted(graph, lastPickedUp)
                        lastCont = cont
                        
                    nodeTo = successors[successorsNumber].getNodeTo()
                    
                    if mode == 0:
                        var1 = (graph[lastPickedUp.getID() - 1][0].getTime() * p) - graph[lastPickedUp.getID() - 1][nodeTo.getID() - 1].getTime() - graph[nodeTo.getID() - 1][0].getTime()
                    elif mode == 1:
                        var1 = graph[lastPickedUp.getID() - 1][0].getTime() + p - graph[lastPickedUp.getID() - 1][nodeTo.getID() - 1].getTime() - graph[nodeTo.getID() - 1][0].getTime()
                    
                    if var1 < 0 or nodeTo.getPickedUp() == True:
                        successorsNumber += 1
                        continue
                    
                    canPickUp = True

                    if nodeTo is not None and nodeTo.getPickedUp() is not True:

                        if (minimum - graph[lastPickedUp.getID()-1][nodeTo.getID()-1].getTime() - graph[nodeTo.getID()-1][0].getTime()) < 0:
                            canPickUp = False

                        if canPickUp:
          
                            countOfInstances = 1
                            baseTime = graph[lastPickedUp.getID()-1][nodeTo.getID()-1].getTime()
                            nodeToCompare = successors[successorsNumber+1].getNodeTo()
                            arrayOfSameTimes = []
                            arrayOfSameTimes.append(graph[lastPickedUp.getID()-1][nodeTo.getID()-1])
                            
                            if  (baseTime == graph[lastPickedUp.getID()-1][nodeToCompare.getID()-1].getTime()):
                                for x in range (1,len(distancesArray)):
                                    if graph[lastPickedUp.getID() - 1][successors[x].getNodeTo().getID()-1].getTime() == baseTime:
                                        if(successors[x].getNodeTo().getPickedUp() is not True):
                                            if minimum - baseTime - graph[successors[x].getNodeTo().getID()-1][0].getTime() >= 0:
                                                countOfInstances+=1
                                                arrayOfSameTimes.append(successors[x])
                                    else:
                                        
                                        break
                                    
                                if countOfInstances > 1:
                                    arrayOfSameTimesSortedByDistance = self.getDistanceFromToSortedD(arrayOfSameTimes)
                                    nodeTo = arrayOfSameTimesSortedByDistance[0].getNodeTo()
                                    
                            countOfInstances = 0
         
                            iniNode.addPassenger(nodeTo)

                            for max in range(len(maxTimesToTarget)):
                                maxTimesToTarget[max] -= graph[lastPickedUp.getID()-1][nodeTo.getID()-1].getTime()
                                minimum = min(minimum,maxTimesToTarget[max])
                            if mode == 0:
                                maxTimesToTarget.append(int(graph[nodeTo.getID() - 1][0].getTime()) * p)
                                minimum = min(minimum,int(graph[nodeTo.getID() - 1][0].getTime()) * p)
                            elif mode == 1:
                                maxTimesToTarget.append(int(graph[nodeTo.getID() - 1][0].getTime()) + p)
                                minimum = min(minimum,int(graph[nodeTo.getID() - 1][0].getTime()) + p)
                            lastPickedUp = nodeTo
                            nodeTo.setPickedUp(True)
                            cont += 1
                            successorsNumber = 0
                        else:
                            successorsNumber += 1

                    else:
                        successorsNumber += 1

    def showAnswer(self, numberOfNodes, p):
        """
        This method writes a file with the answer
        :param numberOfNodes: number of nodes
        :param p: time or percentage that every Node can be delayed
        :return: None
        """
        filename = "./answers/resultCarpoolingRouting-U=" + str(numberOfNodes) + "-p=" + str(p) + ".txt"
        result = open(filename, "w+")
        cont = 0
        for arc in self.__distancesArray:
            node = arc.getNodeFrom()

            if node is not None and len(node.getPassengers()) != 0:
                cont += 1
                nodes = (node.getPassengers())
                contNodes = 0
                result.write("[ ")
                self.__answerMatrix.append([])
                for n in nodes:
                    self.__answerMatrix[cont-1].append(int(n.getID()))
                    contNodes += 1
                    if contNodes < len(nodes):
                        result.write(str(n.getID()) + ", ")
                    else:
                        result.write(str(n.getID()))
                result.write(" ]\n")
        result.write("Number of cars: " + str(cont))
        self.__totalNumberOfCars = cont

    def getDistanceFromToSorted(self, graph, node1):
        """
        This method sorts a given node's neighbors by time
        :param graph: the matrix of arcs
        :param node1: Node to get the sorted array
        :return: the sorted array
        """
        sortedArray = []
        for i in range(len(graph)):
            if i != int(node1.getID() - 1):
                sortedArray.append(graph[int(node1.getID()) - 1][i])
        sortedArray.sort(key=lambda x: int(x.getTime()))
        
        return sortedArray
    
    def getDistanceFromToSortedD(self, array):
        """
        This method sorts a given node's neighbors by distance in metes
        :param array: array of arcs
        :return: the sorted array
        """
        array.sort(key=lambda x: int(x.getDistance()))

        return array

    def printArrayArcos(self, arr):
       if len(arr) == 1:
            print("["+str(arr[0].getNodeTo().getID())+"]") 
       else:
            print("[", end="")
            for i in range(len(arr) - 1):
                print(arr[i].getNodeTo().getID(), end=",")
            print(arr[len(arr) - 1].getNodeTo().getID(), end="")
            print("]")
        
    def printArrayArcosTime(self, arr):
        if len(arr) == 1:
            print("["+str(arr[0].getTime())+"]") 
        else:
            print("[", end="")
            for i in range(len(arr) - 1):
                print(arr[i].getTime(), end=",")
            print(arr[len(arr) - 1].getTime(), end="")
            print("]")

    
    def getAnswerMatrix(self):
        return self.__answerMatrix
    
    def getTotalNumberOfCars(self):
        return self.__totalNumberOfCars