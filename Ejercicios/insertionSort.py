from sys import stdin
from random import randint

LIMIT = 100
SIZE = 10

def insertionIndexBased( indexToSort, sequence):
    elementToSort, beforeElement = sequence[indexToSort], sequence[indexToSort-1]

    while elementToSort < beforeElement and indexToSort > 0:
        sequence[indexToSort], sequence[indexToSort-1] = sequence[indexToSort-1], sequence[indexToSort]
        indexToSort= indexToSort - 1
        elementToSort, beforeElement = sequence[indexToSort], sequence[indexToSort - 1]
def insertionSort( sequence ):
    for index in range(1, len(sequence)):
        insertionIndexBased(index, sequence)
def main():
    sequence = [2,1]
    print('Original: ', sequence)
    insertionSort(sequence)
    print('Ordenada: ',sequence)


main()