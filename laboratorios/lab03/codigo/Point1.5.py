from GraphAL import *
from GraphAM import *
import math


# This class contains a method that determinate if a graph has a loop
class BacktrackingLoop:

    # Auxiliary method to complete the parameters of the principal method
    def loopAux(self, g, init):
        valued = [False]*g.size
        value = self.isThereALoop(g, init, init, valued, 0)
        if value is None:
            return False
        else:
            return value

    # Principal method that determinate if a graph has a loop
    def isThereALoop(self, g, v, w, valued, visited):
        valued[v] = True
        visited += 1
        if v == w and visited > 1:
            return True
        else:
            children = g.getSuccessors(v)
            for son in children:
                if son == w:
                    return True
                else:
                    return self.isThereALoop(g, son, w, valued, visited)


# Tests to try out the algorithm
proof = BacktrackingLoop()
# Create the graph
g1 = GraphAl(5)
g1.addArc(0, 2, 100)
g1.addArc(2, 4, 100)
g1.addArc(0, 1, 15)
g1.addArc(1, 3, 10)
g1.addArc(1, 2, 10)
g1.addArc(0, 3, 20)
g1.addArc(3, 2, 20)
g1.addArc(3, 4, 300)
g1.addArc(4, 0, 300)

g2 = GraphAl(5)
g2.addArc(0, 2, 100)
g2.addArc(2, 4, 100)
g2.addArc(0, 1, 15)
g2.addArc(1, 3, 10)
g2.addArc(1, 2, 10)
g2.addArc(0, 3, 20)
g2.addArc(3, 2, 20)
g2.addArc(3, 4, 300)

# Print the answer
print(proof.loopAux(g1, 0))
print(proof.loopAux(g2, 0))
