from Drawer import *
from OrderFinder import *
from datetime import datetime

class Main:
    
    __p = 0
    __numberOfCars = 0
    
    def main(self, fileName, nCars, type1, type2, type3):
        
        drawerTEST = DrawerTEST()
        test = Graph()
        result = OrderFinder()
        """U = "205"
        nCars = int(U)
        P = "5"
        fileToUse = "-U="+U+"-p="+P+".txt"""
        size = 25
        
        print("Times")
        startTime = datetime.now()
        #test.readGraph("./dataSets/dataset-ejemplo"+fileToUse, nCars)
        test.readGraph(fileName, nCars)
        print("Read graph: " + str(datetime.now() - startTime))
        startTime = datetime.now()
        distances = result.getTargetDistance(test.getMatrix())
        print("Get target distance: " + str(datetime.now() - startTime))
        startTime = datetime.now()
        result.orderFinder(distances, test.getMatrix(), test.getP(), test.getMode())
        print("Order finder: " + str(datetime.now() - startTime))
        startTime = datetime.now()
        result.showAnswer(test.getNumberOfNodes(), test.getP())
        print("Show answer: " + str(datetime.now() - startTime))
        self.__p = test.getP()
        self.__numberOfCars = result.getTotalNumberOfCars() 
        print("Answer for p = " + str(test.getP()) + " is: "+str(result.getTotalNumberOfCars()))
        center = [test.getTargetLat(), test.getTargetLon()]
        
        pruebaLat = []
        pruebaLon = []
        ids = []
        answerMatrix = result.getAnswerMatrix()
        numberCarsAnswer = result.getTotalNumberOfCars()
        lats = []
        longs = []
        
        for i in range(len(answerMatrix) - 1):# -1 because for some reason the answer matrix has an empty array at the end
            
            for j in range(len(answerMatrix[i])):
                
                lats.append(test.getMatrix()[answerMatrix[i][j] - 1 ][0].getNodeFrom().getLatitude())
                longs.append(test.getMatrix()[answerMatrix[i][j] - 1 ][0].getNodeFrom().getLongitude())
                pruebaLat.append(test.getMatrix()[answerMatrix[i][j] - 1 ][0].getNodeFrom().getLatitude())
                pruebaLon.append(test.getMatrix()[answerMatrix[i][j] - 1 ][0].getNodeFrom().getLongitude())
                ids.append(str(test.getMatrix()[answerMatrix[i][j] - 1 ][0].getNodeFrom().getID()))
                
            pruebaLat.append(0.0)
            pruebaLon.append(0.0)
            
        ids.append(str(test.getMatrix()[0][0].getNodeFrom().getDescription()))
        targetLatitudes = test.getTargetLat()
        targetLongitudes = test.getTargetLon()
        lats.append(targetLatitudes)
        longs.append(targetLongitudes)
        latitudes = pd.Series(lats)
        longitudes = pd.Series(longs)
        color = np.array(np.sqrt((latitudes-(targetLatitudes))**2+(longitudes-(targetLongitudes))**2)).reshape((-1, 1))
        
        if type1:
            drawerTEST.plot_map((pruebaLat), (pruebaLon), ids, 1 , center, color, size)    
        if type2:
            drawerTEST.plot_map((pruebaLat), (pruebaLon), ids, 2 , center, color, size)
        if type3:
            drawerTEST.plot_map((pruebaLat), (pruebaLon), ids, 3 , center, color, size)

    def getP(self):
        return self.__p
    
    def getTotalNumberOfCars(self):
        return self.__numberOfCars

