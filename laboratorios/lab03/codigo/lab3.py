import sys
import time
class Lab3:

    def oneSolutionNqueens(self,  board, n, row):
        if(row==n):
            for i in range(n):
                for j in range(n):
                    print(board[i][j]+ " ", end='')
                print("")
            return True
        for i in range(n):
            if(self.canPlaceQueen(board, row, i, n)):
                board[row][i] = 'Q'
                recCall = self.oneSolutionNqueens(board, n, row+1)
                if recCall:
                    return True
                board[row][i] = '*'
        return False

    def canPlaceQueen(self, board, row, col, n):
        for i in range(0,n):
            if(board[i][col]=='Q'):
                return False

        for i in range(0,n):
            if (board[row][i]  == 'Q'):
                return False

        i = row
        j = col
        while (i >=0 and j >= 0):
            if (board[i][j] == 'Q'):
                return False
            j-=1
            i-=1
        i = row
        j = col
        while (i >=0 and j < n):
            if (board[i][j] == 'Q'):
                return False
            j+=1
            i-=1
        i = row
        j = col
        while (j >=0 and i < n):
            if (board[i][j] == 'Q'):
                return False
            j-=1
            i+=1
        i = row
        j = col
        while (i <n and j <n):
            if (board[i][j] == 'Q'):
                return False
            j+=1
            i+=1
        return True


    def getIntInput(self):
        boardLength = input("Enter the board's length ")
        try:
            val = int(boardLength)
            return val

        except ValueError:
            print("That's not an int!, try again")
            return self.getIntInput()

    def mainMethod(self, n):
        boardLength = n
        board = [['*' for i in range(boardLength)] for j in range(boardLength)]
        self.oneSolutionNqueens(board,boardLength,0)

test = Lab3()
test.mainMethod(10)
times = ['']*32
cont = 0
for i in range(4,32):
    start = time.time()
    test.mainMethod(i)
    end = time.time()
    total = end - start
    print("For n = " + str(i) + " time is = to " + str(total))
    times[cont]=str("For n = "+str(i)+" time is = to "+str(total))
    cont+=1
    start = 0
    end = 0
    total = 0
for i in range(len(times)):
    print(str(times[i]))