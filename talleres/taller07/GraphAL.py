class GraphAl:
    size = 0
    def __init__(self, size):
        self.size = size
        self.graph = {}
        for i in range(self.size):
            self.graph[i] = []


    def addArc(self, vertex, edge, weight):
        # Add a edge in vertex if vertex exists
        try:
            self.graph[vertex].append((edge, weight))
        except KeyError:
            # Here vertex is no in graph
            pass

    def getSuccessors(self, vertice):
        list = []
        for i in self.graph[vertice]:
            list.append(i[0])
        return list

    def getWeight(self, source, destination):
        for i in self.graph[source]:
            if(i[0] == destination):
                return i[1]

    def __str__(self):
        # Print the vertex
        s = "Vertex -> Edges\n"
        for k, v in self.graph.items():
            s += "%-6s -> %s\n" % (k, v)
        return s

