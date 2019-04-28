from Graph import *
from Arc import *
from Node import *
from OrderFinder import *

test = Graph()
result = OrderFinder()

test.readGraph("./dataSets/dataset-ejemplo-U=205-p=1.1.txt", 205)
distances = result.getTargetDistance(test.getMatrix())
result.orderFinder(distances, test.getMatrix(), test.getP())
result.showAnswer()

