# -*- coding: utf-8 -*-
from Arc import *
from Node import *
import math

"""
 * This class contains the methods that read the file and save the graph for later access.
 *
 * @author Juan Sebastián Pérez Salazar
   @author Yhoan Alejandro Guzmán García
"""
class Graph:

    __graph = {}
    __matrix = [[]]
    __distanceLongi = 111111
    __distanceLat = 111000
    __p = 1
    __cars = 0
    __mode = 0
    __nodesArray = []

    """
    * This method reads the file and generateS the graph
    * @param fileName name of the file with vertices and edges
    """
    def readGraph(self, filename, numberOfCars):
        self.__cars = numberOfCars
        try:
            file = open(filename, "r", encoding='utf-8')
            strP = file.readline().split(" ")[1]
            try:
                self.__p = int(strP)
                self.__mode = 1
            except ValueError:
                self.__p = float(strP)
                self.__mode = 0
            for i in range(4):
                line = file.readline()
            cont = 0
            while line != "" and line != "\n":
                cont += 1
                #print(line)
                if len(line) > 0 and line != "\n":
                    if "Costo" in line:
                        break
                    description = ""
                    lineArray = line.split(" ")
                    if len(lineArray) >= 4:
                        description = lineArray[3]
                    node = Node(int(lineArray[0]), float(lineArray[1]), float(lineArray[2]), description)
                    self.__graph[node.getID()] = node
                    self.__nodesArray.append(node)
                line = file.readline()
            print("Number of read nodes: " + str(cont))
            for i in range(3):
                line = file.readline()
            self.__matrix = [[Arc(0, 0, 0, None, None) for x in range(numberOfCars)] for y in range(numberOfCars)]
            while line != "" and line != "\n":
                if len(line) > 0:
                    lineArray = line.split(" ")
                    node1 = self.__graph.get(int(lineArray[0]))
                    node2 = self.__graph.get(int(lineArray[1]))
                    arc = Arc(lineArray[2], self.getAngle(node1, node2), self.getDistanceBNodes(node1, node2),
                              node1, node2)
                    self.__matrix[int(lineArray[0])-1][int(lineArray[1])-1] = arc
                line = file.readline()
            file.close()
            for node in self.__nodesArray:
                arc = Arc(0, 0, 0, node, node)
                self.__matrix[int(node.getID()) - 1][int(node.getID()) - 1] = arc
        except:
            print("An error occurred while reading the file")

    def getAngle(self, node1, node2):
        try:
            return math.asin(self.getDBetweenNodesLat(node1, node2) /
                             self.__matrix[node1.getID()-1][node2.getID()-1].getDistance())
        except Exception:
            return 0

    def getDBetweenNodesLat(self, node1, node2):
        return math.fabs(math.fabs(node1.getLatitude()) - math.fabs(node2.getLatitude()))*self.__distanceLat



    def getDistanceBNodes(self, node1, node2):
        distanceBLongitudes = (math.fabs(math.fabs(node1.getLongitude()) - math.fabs(node2.getLongitude())) * self.__distanceLongi)
        distanceBLatitudes = (math.fabs(math.fabs(node1.getLatitude()) - math.fabs(node2.getLatitude())) * self.__distanceLat)
        return math.sqrt(pow(distanceBLatitudes, 2)+pow(distanceBLongitudes, 2))

    def getMatrix(self):
        return self.__matrix

    def getP(self):
        return self.__p

    def getCars(self):
        return self.__cars

    def getMode(self):
        return self.__mode

    def printMatrix(self):
        matrix = self.__matrix
        for i in range(len(self.__matrix)):
            print("[   ", end="")
            for j in range(len(self.__matrix)):
                print(str(matrix[i][j].getNodeFrom()) + "  ,  ", end = "")
            print(" ]")



prueba = Graph()
prueba.readGraph("./dataSets/dataset-ejemplo-U=4-p=1.2.txt", 5)
#prueba.readGraph("./dataSets/dataset-ejemplo-U=4-p=1.2.txt", 5)
#prueba.printMatrix()

