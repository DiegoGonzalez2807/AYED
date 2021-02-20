from sys import stdin

def printResultMatrix(resultMatrix):                           #COST       PASOS
    for row in resultMatrix:                                   # 1           n
        print(' '.join(map(str, row)))                         # 1           n-1
                                                               # TOTAL =1*n + 1*(n-1)
                                                               # TOTAL = n + n - 1
                                                               # TOTAL = 2n -1 ---> O(n)


def calculateCellsDistance(i,j, dimension):                    #COST        PASOS
    center = dimension // 2                                    #1             1
    return 1 + max(abs(i-center), abs(j-center))               #1             1
                                                               #TOTAL = 1 + 1 = 2 ----> O(1)



def solveWonderSquare(n):                                                                                               #COST          PASOS
    dimension = 2*n -1                                                                                                  #  1              1
    resultMatrix = [[calculateCellsDistance(i,j, dimension) for j in range(dimension)] for i in range(dimension)]       #  1             n^2
    return resultMatrix                                                                                                 #  1              1
                                                                                                                        #   TOTAL = 1*1 + 1*n^2 + 1*1
                                                                                                                        # TOTAL = 1 + n^2 + 1 ----> O(n^2)



def main():                                               #COST       PASOS
    line = stdin.readline()                               #  1           1
    while line:                                           #  1           n
        n = int(line.strip())                             #  1           n-1
        resultMatrix = solveWonderSquare(n)               #  n^2         n-1
        printResultMatrix(resultMatrix)                   #  n           n-1
        line = stdin.readline()                           #  1           n-1
                                                          #TOTAL = 1 + n + n - 1 + n^2(n-1) + n(n-1) + n - 1
                                                          #TOTAL = 2n + n^3 - n^2 + n^2 - n + n - 1
                                                          #TOTAL = n^3 +2n -1 -----> O(n^3)
main()