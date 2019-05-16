from Arc import *
from Node import *
import math

class Graph:
    """
    This class reads the file and stores the data in a matrix using Arcs and Nodes

    :author Juan Sebastian  Perez Salazar
    :author Yhoan Alejandro Guzman Garcia
    """

    __graph = {}
    __matrix = [[]]
    __distanceLongi = 111111
    __distanceLat = 111000
    __p = 1
    __numberNodes = 0
    __mode = 0
    __nodesArray = []
    __latArray = []
    __lonArray = []
    __promLon = 0.0
    __promLat = 0.0
    __targetLat = 0.0
    __targetLon = 0.0

    def readGraph(self, filename, numberOfNodes):
        """
        This method reads the file and creates the graph, storing it in a matrix
        :param filename: name of the file that will be open
        :param numberOfNodes: number of node that will be read
        :return: None
        """

        self.__numberNodes = numberOfNodes
        latSum = 0.0
        lonSum = 0.0
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

                if len(line) > 0 and line != "\n":

                    if "Costo" in line:
                        break

                    description = ""
                    lineArray = line.split(" ")

                    if len(lineArray) >= 4:
                        description = lineArray[3]

                    node = Node(int(lineArray[0]), float(lineArray[1]), float(lineArray[2]), description)
                    lonSum += float(lineArray[1])
                    latSum += float(lineArray[2])

                    self.__graph[node.getID()] = node
                    self.__nodesArray.append(node)
                    self.__lonArray.append(float(lineArray[1]))
                    self.__latArray.append(float(lineArray[2]))

                line = file.readline()

            self.__promLon = lonSum / numberOfNodes
            self.__promLat = latSum / numberOfNodes

            self.__distanceLongi = self.getDistanceBetweenLongitudesG(self.__promLat)
            
            for i in range(3):
                line = file.readline()

            self.__matrix = [[Arc(0, 0, None, None) for x in range(numberOfNodes)] for y in range(numberOfNodes)]

            while line != "" and line != "\n":

                if len(line) > 0:
                    lineArray = line.split(" ")
                    node1 = self.__graph.get(int(lineArray[0]))
                    node2 = self.__graph.get(int(lineArray[1]))
                    arc = Arc(lineArray[2], self.getDistanceBNodes(node1, node2), node1, node2)
                    self.__matrix[int(lineArray[0])-1][int(lineArray[1])-1] = arc

                line = file.readline()
                
            file.close()
            for node in self.__nodesArray:
                arc = Arc(0, 0, node, node)
                self.__matrix[int(node.getID()) - 1][int(node.getID()) - 1] = arc

        except:
            print("An error occurred while reading the file")

        self.__targetLat = self.__matrix[0][0].getNodeFrom().getLatitude()
        self.__targetLon = self.__matrix[0][0].getNodeFrom().getLongitude()
        
        
    def getDistanceBNodes(self, node1, node2):
        """
        This method calculates the distance between the nodes
        :param node1: node object from
        :param node2: node object to
        :return: The distance between the nodes
        """
        distanceBLongitudes = (math.fabs(math.fabs(node1.getLongitude()) - math.fabs(node2.getLongitude())) * self.__distanceLongi)
        distanceBLatitudes = (math.fabs(math.fabs(node1.getLatitude()) - math.fabs(node2.getLatitude())) * self.__distanceLat)
        return math.sqrt(pow(distanceBLatitudes, 2)+pow(distanceBLongitudes, 2))

    def getMatrix(self):
        return self.__matrix
    
    def getLonArray(self):
        return self.__lonArray
    
    def getLatArray(self):
        return self.__latArray
    
    def getPromLon(self):
        return self.__promLon
    
    def getPromLat(self):
        return self.__promLat
    
    def getTargetLon(self):
        return self.__targetLon
    
    def getTargetLat(self):
        return self.__targetLat
    
    def getP(self):
        return self.__p

    def getNumberOfNodes(self):
        return self.__numberNodes

    def getMode(self):
        return self.__mode

    def printMatrix(self):
        """
        This method prints the matrix that stores the Arcs
        :return: None
        """
        matrix = self.__matrix
        for i in range(len(self.__matrix)):
            print("[   ", end="")
            for j in range(len(self.__matrix)):
                print(str(matrix[i][j].getNodeFrom()) + "  ,  ", end = "")
            print(" ]")
                
    def getDistanceBetweenLongitudesG(self, average):
        return -3 * math.pow(10, -9) * math.pow(average, 6) - 2 * math.pow(10, -7) * math.pow(average, 5) + 0.0004 * math.pow(average, 4) - 0.0005 * math.pow(average, 3) - 16.948 * math.pow(average, 2) - 0.0463 * average + 111325;