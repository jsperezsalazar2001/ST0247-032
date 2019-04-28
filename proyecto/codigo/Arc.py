

"""
This class is the arc or edge object
@author Yhoan Alejandro Guzmán García
@author Juan Sebastián Pérez
"""


class Arc:


    """
     * Class constructor
     * @param nodeIDFrom name of the first node
     * @param nodeIDTo name of the second node
     * @param distance distance between nodes
     * @param name street name
    """
    def __init__(self, time, angle, distance, nodeFrom, nodeTo):
        self.__nodeFrom = nodeFrom
        self.__nodeTo = nodeTo
        self.__time = time
        self.__angle = angle
        self.__distance = distance

    def getTime(self):
        return int(self.__time)

    def setTime(self, time):
        self.__time = time

    def getAngle(self):
        return self.__angle

    def setAngle(self, angle):
        self.__angle = angle

    def getDistance(self):
        return self.__distance

    def setDistance(self, distance):
        self.__distance = distance

    def getNodeFrom(self):
        return self.__nodeFrom

    def getNodeTo(self):
        return self.__nodeTo

