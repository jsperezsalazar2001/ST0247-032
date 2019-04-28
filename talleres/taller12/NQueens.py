import random, copy

"""
	@author Juan Sebastián Pérez Salazar
	@author Yhoan Alejandro Guzmán García
    This algorithm is based in an algorithm taken from 'https://webstersprodigy.net/2009/10/31/8-queens-problem-hill-climbing-python/'
"""

class Board:

    __n = 0

    def __init__(self, list=None, n=8):
        self.__n = n
        if list is None:
            self.board = [[0 for i in range(0, n)] for j in range(0, n)]
            # initialize queens at random places
            for i in range(0, n):
                while 1:
                    rand_row = random.randint(0, n-1)
                    rand_col = random.randint(0, n-1)
                    if self.board[rand_row][rand_col] == 0:
                        self.board[rand_row][rand_col] = "Q"
                        break

    # define how to print the board
    def __repr__(self):
        mstr = ""
        for i in range(0, self.__n):
            for j in range(0, self.__n):
                mstr = mstr + str(self.board[i][j]) + " "
            mstr = mstr + "\n"
        return mstr


class Queens:

    def __init__(self, numruns, verbocity, n, passedboard=None):
        # TODO check options
        self.totalruns = numruns
        self.totalsucc = 0
        self.totalnumsteps = 0
        self.verbocity = verbocity
        for i in range(0, numruns):
            if self.verbocity == True:
                print("====================")
                print("BOARD", i)
                print("====================")
            self.mboard = Board(passedboard, n)
            self.cost = self.calc_cost(self.mboard, n)
            self.hill_solution(n)

    def hill_solution(self, n):
        while 1:
            currViolations = self.cost
            self.getlowercostboard(n)
            if currViolations == self.cost:
                break
            self.totalnumsteps += 1
            if self.verbocity is True:
                print("Board Violations", self.calc_cost(self.mboard, n))
                print(self.mboard)
        if self.cost != 0:
            if self.verbocity is True:
                print("NO SOLUTION FOUND")
        else:
            if self.verbocity is True:
                print("SOLUTION FOUND")
            self.totalsucc += 1
        return self.cost

    def printstats(self):
        print("Total Runs: ", self.totalruns)
        print("Total Success: ", self.totalsucc)
        print("Success Percentage: ", float(self.totalsucc) / float(self.totalruns))
        print("Average number of steps: ", float(self.totalnumsteps) / float(self.totalruns))

    def calc_cost(self, tboard, n):
        # these are separate for easier debugging
        totalhcost = 0
        totaldcost = 0
        for i in range(0, n):
            for j in range(0, n):
                # if this node is a queen, calculate all violations
                if tboard.board[i][j] == "Q":
                    # subtract 2 so don't count self
                    # sideways and vertical
                    totalhcost -= 2
                    for k in range(0, n):
                        if tboard.board[i][k] == "Q":
                            totalhcost += 1
                        if tboard.board[k][j] == "Q":
                            totalhcost += 1
                    # calculate diagonal violations
                    k, l = i + 1, j + 1
                    while k < n and l < n:
                        if tboard.board[k][l] == "Q":
                            totaldcost += 1
                        k += 1
                        l += 1
                    k, l = i + 1, j - 1
                    while k < n and l >= 0:
                        if tboard.board[k][l] == "Q":
                            totaldcost += 1
                        k += 1
                        l -= 1
                    k, l = i - 1, j + 1
                    while k >= 0 and l < n:
                        if tboard.board[k][l] == "Q":
                            totaldcost += 1
                        k -= 1
                        l += 1
                    k, l = i - 1, j - 1
                    while k >= 0 and l >= 0:
                        if tboard.board[k][l] == "Q":
                            totaldcost += 1
                        k -= 1
                        l -= 1
        return (totaldcost + totalhcost) / 2

    # this function tries moving every queen to every spot, with only one move
    # and returns the move that has the leas number of violations
    def getlowercostboard(self, n):
        lowcost = self.calc_cost(self.mboard, n)
        lowestavailable = self.mboard
        # move one queen at a time, the optimal single move by brute force
        for q_row in range(0, n):
            for q_col in range(0, n):
                if self.mboard.board[q_row][q_col] == "Q":
                    # get the lowest cost by moving this queen
                    for m_row in range(0, n):
                        for m_col in range(0, n):
                            if self.mboard.board[m_row][m_col] != "Q":
                                # try placing the queen here and see if it's any better
                                tryboard = copy.deepcopy(self.mboard)
                                tryboard.board[q_row][q_col] = 0
                                tryboard.board[m_row][m_col] = "Q"
                                thiscost = self.calc_cost(tryboard, n)
                                if thiscost < lowcost:
                                    lowcost = thiscost
                                    lowestavailable = tryboard
        self.mboard = lowestavailable
        self.cost = lowcost


mboard = Queens(7, True, 8)
mboard.printstats()