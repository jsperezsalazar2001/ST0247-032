from Arc import *
from Node import *

"""
 * This class contains the methods that read the file and save the graph for later access.
 *
 * @author Juan Sebastián Pérez Salazar
   @author Yhoan Alejandro Guzmán García
"""
class Graph:

    __graph = {}
    __distanceLongi = 111111
    __distanceLat = 111000
    """
    * This method reads the file and generateS the graph
    * @param fileName name of the file with vertices and edges
    """
    def readGraph(self, filename, numberOfCars):
        try:
            file = open(filename, "r")
            for i in range(5):
                line = file.readline()
            while line is not None:
                if len(line) > 0:
                    if "Costo" in line:
                        break
                    description = ""
                    lineArray = line.split(" ")
                    if len(lineArray) >= 4:
                        description = lineArray[3]
                    node = Node(lineArray[0], float(lineArray[1]), float(lineArray[2]), description)
                    self.__graph.add(node.getID(), node)
            for i in range(2):
                line = file.readline()
                matrix = [[0 for x in range(numberOfCars)] for y in range(numberOfCars)]
            while line is not None:
                if len(line) > 0:
                    lineArray = line.split(" ")
                    node1 = self.__graph.get(lineArray[0])
                    node2 = self.__graph.get(lineArray[1])
                    arc = Arc(lineArray[2], self.getAngle(node1, node2), self.getDistanceBNodes(node1, node2,111111))
                    matrix[int(lineArray[0])-1][int(lineArray[1])-1] = arc
        except:
            print("error gonorrea")

    def getAngle(self, node1, node2):
        return (node2.getLatitude() - node1.getLatitude())/(node2.getLongitude() - node1.getLongitude())

    """def getDistance(self, node1, node2, average):
        return -3 * pow(10, -9) * pow(average, 6) - 2 * pow(10, -7) * pow(average, 5) + 0.0004 * pow(average, 4) - 0.0005 * pow(average, 3) - 16.948 * pow(average, 2) - 0.0463 * average + 111325;"""

    def getDistanceBNodes(self, node1, node2):
        distanceBLongitudes = (abs(abs(node1.getLongitude) - abs(node2.getLongitude)) * self.__distanceLongi)
        distanceBLatitudes = (abs(abs(node1.getLatitude) - abs(node2.getLatitude)) * self.__distanceLat)
        return sqrt(pow(distanceBLatitudes,2)+pow(distanceBLongitudes,2))
