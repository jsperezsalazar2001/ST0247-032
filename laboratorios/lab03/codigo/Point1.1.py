from GraphAL import *
from GraphAM import *
import math

# This class contains a method that find the path with the minimum cost from vertex A to vertex B
class BacktrackingMinCost:

    # Auxiliary method to complete the parameters of the principal method
    def minumumCostAux(self, g, init, end):
        valued = [False]*g.size
        cost = self.minimumCost(g, init, end, math.inf, 0, valued)
        if cost == math.inf:
            return "There is not a path"
        else:
            return cost

    # Principal method that find the path with the minimum cost and return it
    def minimumCost(self, g, v, w, minCost, accumulated, valued):
        valued[v] = True
        if v == w:
            if minCost > accumulated:
                minCost = accumulated
            return minCost
        else:
            children = g.getSuccessors(v)
            for son in children:
                fatherSonCost = g.getWeight(v, son)
                if (fatherSonCost < minCost) and (v != son) and valued[son] is False:
                    minCost = min(self.minimumCost(g, son, w, minCost, accumulated + g.getWeight(v, son), valued), minCost)
                    valued[son] = False
            return minCost


# Tests to try out the algorithm
proof = BacktrackingMinCost()
# Create the graph
g1 = GraphAl(5)
g1.addArc(0, 2, 100)
g1.addArc(2, 0, 100)
g1.addArc(2, 4, 100)
g1.addArc(0, 1, 15)
g1.addArc(1, 3, 10)
g1.addArc(1, 2, 10)
g1.addArc(0, 3, 20)
g1.addArc(3, 2, 20)
g1.addArc(3, 4, 300)
# Print the answer
print(proof.minumumCostAux(g1, 0, 4))
