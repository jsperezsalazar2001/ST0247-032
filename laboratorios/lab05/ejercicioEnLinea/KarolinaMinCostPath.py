import math

class Trash:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = 0
        self.collected = False

class minCostPath:

    def minCost(self, x, y, m, n):

        if y > n:
            tp = y
            y = n
            n = tp
        if x > m:
            tp = x
            x = m
            m = tp

        return (m-x) + (n-y)

    def printMatrix(self, matrix, m, n):
        for i in range(0, m):
            print("[", end="")
            for j in range(0, n):
                print(matrix[i][j], end=",")
            print(" ]")

    def readFile(self, filename):
        file = open(filename, "r", encoding='utf-8')
        line = file.readline()
        list = []
        executions = int(line)
        for j in range(executions):
            size = file.readline().split(" ")
            robot = file.readline().split(" ")
            x = int(robot[0])
            y = int(robot[1])

            numberOfTrash = int(file.readline())
            for i in range(numberOfTrash):
                trash = file.readline().split(" ")
                list.append(Trash(int(trash[0]), int(trash[1])))
            self.finder(list, x, y)
            list = []

    def finder(self, list, x, y):
        sum = 0
        longitude = len(list)
        x1 = x
        y1 = y
        for iteration in range(longitude):
            for i in list:
                if i.collected is False:
                    i.distance = self.minCost(x, y, i.x, i.y)
            list.sort(key=lambda z: z.distance)
            x = list[0].x
            y = list[0].y
            list[0].collected = True
            print(list[0].distance)
            if len(list) > 1:
                sum += list.pop(0).distance
            else:
                sum += list[0].distance
                sum += self.minCost(x1, y1, list[0].x, list[0].y)

        print(sum)


test = minCostPath()
test.readFile("test1.txt")

