class Arc:
    """
        This class is the arc or edge object
        :author Yhoan Alejandro Guzmán García
        :author Juan Sebastián Pérez
    """

    def __init__(self, time, distance, nodeFrom, nodeTo):
        """
        Class constructor
        :param time: time between the nodes
        :param distance: distance between the nodes in meters
        :param nodeFrom: node object from
        :param nodeTo: node object to
        """

        self.__nodeFrom = nodeFrom
        self.__nodeTo = nodeTo
        self.__time = time
        self.__distance = distance

    def getTime(self):
        return int(self.__time)

    def setTime(self, time):
        self.__time = time

    def getDistance(self):
        return self.__distance

    def setDistance(self, distance):
        self.__distance = distance

    def getNodeFrom(self):
        return self.__nodeFrom

    def getNodeTo(self):
        return self.__nodeTo

