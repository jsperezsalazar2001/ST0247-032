"""
 * This class is the node object.
 * @author Yhoan Alejandro Guzmán García
 * @author Juan Sebastián Pérez
 """


class Node:
    """
     * Class constructor.
     * @param ID node identifier.
     * @param longitude node longitude
     * @param latitude node latitude
     * @param name node name
     """

    def __init__(self, id, lon, lat, nam):
        self.__ID = id
        self.__longitude = lon
        self.__latitude = lat
        self.__name = nam
        self.__neighbors = [()]

    def getID(self):
        return self.__ID

    def setID(self, id):
        self.__ID = id

    def getLongitude(self):
        return self.__longitude

    def setLongitude(self, lon):
        self.__longitude = lon

    def getLatitude(self):
        return self.__latitude

    def setLatitude(self, lat):
        self.__latitude = lat

    def getName(self):
        return self.__name

    def setName(self, nam):
        self.__name = nam

    """
     * This method add a new neighbor(creates an edge between two nodes).
     * @param neighbor the other node
     * @param arc edge between nodes
    """

    def addNeighbor(self, neighbor, arc):
        pair = (neighbor, arc)
        self.__neighbors.append(pair)

    """
     * This method get the adyacent nodes of one vertex. 
     * @return a linkedList
    """

    def getNeighbors(self):
        return self.__neighbors