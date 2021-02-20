from sys import stdin
import math


def findMaxCharacter(word):                                                                         # COST       PASOS
    maxCharacter, maxOcurrencies = None, -math.inf                                                  #   1          1
    alphabet = {} #Malloc                                                                           #   1          1
    for character in word:                                                                          #   1          n
        alphabet[character] = alphabet[character] + 1 if character in alphabet.keys() else 1        #   1          n-1
        if maxOcurrencies < alphabet[character]:                                                    #   1          n-1
            maxOcurrencies, maxCharacter = alphabet[character], character                           #   1          n-1
    return maxOcurrencies, maxCharacter                                                             #   1          1
                                                                                                #TOTAL = 1 +1 +n + n - 1 + n - 1 + n - 1 + 1
                                                                                                #TOTAL + 4n ----> O(n)

def main():                                                                                         #COST         PASOS
    word = stdin.readline().strip()                                                                 #   1           1
    print(findMaxCharacter(word))                                                                   #   4n          1
main()                                                                                         #TOTAL = 1 + 4n
                                                                                               #TOTAL = 4n ----> O(n)