#Diego Alejandro Gonzalez Gualteros
#2163199
#C.C. 1007196603
#PUNTO3 CUPIDO
from sys import stdin
import math
def length(array,length_lolouch,comparation):
    if len(array) == 1 and array[0] >= length_lolouch:
        return 'X'
    elif len(array) == 1 and array[0] < length_lolouch:
        return array[0]
    middle = len(array) //2
    if array[middle] >= length_lolouch:
        comparation = array[middle]
        return length(array[:middle],length_lolouch,comparation)
    elif array[middle] <  length_lolouch:
        comparation = array[middle]
        return length(array[middle:], length_lolouch,comparation)
def main():
    length_array = int(stdin.readline().strip())
    array = list(map(int,stdin.readline().strip().split()))
    cases = int(stdin.readline().strip())
    lolouch = list(map(int,stdin.readline().strip().split()))
    if length_array == len(array):
        for lengths in lolouch:
            comparation = 0
            answer = length(array,lengths,comparation)
            print(answer)
main()