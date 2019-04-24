from Graph import *
from Arc import *
from Node import *
from OrderFinder import *

test = Graph()
result = OrderFinder()

test.readGraph("./dataSets/dataset-ejemplo-U=4-p=1.2.txt", 4)
distances = result.getTargetDistance(test.getMatrix())
result.orderFinder(distances, test.getMatrix(), test.getP())
result.showAnswer()

