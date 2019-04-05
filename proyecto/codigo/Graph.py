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
    """
    * This method reads the file and generateS the graph
    * @param fileName name of the file with vertices and edges
    """
    def readGraph(self, filename, numberOfCars):
        try:
            file = open(filename, "r", encoding='utf-8')
            for i in range(5):
                line = file.readline()
            while line != "":
                if len(line) > 0 and line != "\n":
                    if "Costo" in line:
                        break
                    description = ""
                    lineArray = line.split(" ")
                    if len(lineArray) >= 4:
                        description = lineArray[3]
                    node = Node(int(lineArray[0]), float(lineArray[1]), float(lineArray[2]), description)
                    self.__graph[node.getID()] = node
                line = file.readline()
            for i in range(2):
                line = file.readline()
                self.__matrix = [[Arc(0, 0, 0, 0, 0) for x in range(numberOfCars+1)] for y in range(numberOfCars+1)]
            while line != "":
                if len(line) > 0:
                    lineArray = line.split(" ")
                    node1 = self.__graph.get(lineArray[0])
                    node2 = self.__graph.get(lineArray[1])
                    arc = Arc(lineArray[2], self.getAngle(node1, node2), self.getDistanceBNodes(node1, node2),
                              node2.getID(), node1.getID())
                    self.__matrix[int(lineArray[0])-1][int(lineArray[1])-1] = arc
                line = file.readline()
            file.close()
        except:
            print("error gonorrea")

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


prueba = Graph()
prueba.readGraph("dataset-ejemplo-U=4-p=1.2.txt", 4)
print("finish")
