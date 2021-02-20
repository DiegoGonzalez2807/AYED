from sys import stdin
def swapping(sequence):
    count = 0
    for indexToSort in range(1, len(sequence)):
        elementToSort, beforeElement = sequence[indexToSort], sequence[indexToSort - 1]
        while elementToSort < beforeElement and indexToSort > 0:
            sequence[indexToSort], sequence[indexToSort - 1] = sequence[indexToSort - 1], sequence[indexToSort]
            indexToSort = indexToSort - 1
            elementToSort, beforeElement = sequence[indexToSort], sequence[indexToSort - 1]
            count += 1
    return count
def main():
    cases = int(stdin.readline().strip())
    for case in range(cases):
        stdin.readline()
        train = list(map(int, stdin.readline().strip().split()))
        swap = swapping(train)
        print('Optimal train swapping takes ' + str(swap) + ' swaps')
main()



#def spaces(m,n):
    #m,n = min(m,n),max(m,n)
    #answer = [number for number in range(m,n+1)]
    #posibility = []
   # for num in answer:
        #posibility = posibility + [Recursivity(num)]
   # return max(posibility)


# answer = spaces(line[0],line[1])
# print(line[0],line[1],answer)
# line = list(map(int, stdin.readline().strip().split()))
