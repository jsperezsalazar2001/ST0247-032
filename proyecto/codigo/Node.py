class Node:
    """
     This class is the Node object
     :author Juan Sebastian Perez Salazar
     :author Yhoan Alejandro Guzman Garcia
     """

    def __init__(self, id, lon, lat, description):
        """
        Class constructor
        :param id: identifier of the Node
        :param lon: longitudinal position of the Node
        :param lat: latitudinal position of the Node
        :param description: Node's description
        """
        self.__ID = id
        self.__longitude = lon
        self.__latitude = lat
        self.__description = description
        self.__passengers = []
        self.__pickedUp = False

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

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description

    def addPassenger(self, passenger):
        """
        This method adds a new passenger
        :param passenger: is a Node object that is picked up
        :return: None
        """
        self.__passengers.append(passenger)

    def getPassengers(self):
        return self.__passengers

    def getNumberPassenger(self):
        return len(self.__passengers)

    def getPickedUp(self):
        return self.__pickedUp

    def setPickedUp(self, b):
        self.__pickedUp = b
