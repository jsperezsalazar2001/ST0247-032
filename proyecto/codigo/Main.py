from Graph import *
from Arc import *
from Node import *
from OrderFinder import *

test = Graph()
result = OrderFinder()

#test.readGraph("./dataSets/dataset-ejemplo-U=4-p=1.2.txt", 5)  # 2
#test.readGraph("./dataSets/dataset-ejemplo-U=4-p=1.7.txt", 5)  # 2
#test.readGraph("./dataSets/dataset-ejemplo-U=11-p=1.1.txt", 11)  # 4
#test.readGraph("./dataSets/dataset-ejemplo-U=11-p=1.2.txt", 11)  # 4
#test.readGraph("./dataSets/dataset-ejemplo-U=11-p=1.3.txt", 11)  # 3
#test.readGraph("./dataSets/dataset-ejemplo-U=205-p=1.1.txt", 205)  # 60
test.readGraph("./dataSets/dataset-ejemplo-U=205-p=1.2.txt", 205)  # 55
#test.readGraph("./dataSets/dataset-ejemplo-U=205-p=1.3.txt", 205)  # 47
distances = result.getTargetDistance(test.getMatrix())
result.orderFinder(distances, test.getMatrix(), test.getP(), test.getMode())
result.showAnswer(test.getCars(), test.getP())

