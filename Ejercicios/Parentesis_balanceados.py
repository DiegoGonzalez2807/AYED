#Diego Alejandro Gonzalez Gualteros
#2163199
#1007196603
from sys import stdin
class Pila:
    def __init__(self):
        self.list = []

    def empty(self):
        return True if self.list == [] else False

    def push(self,newvalue):
        self.list.append(newvalue)

    def pop(self):
        self.list.pop()

def balanced(array_parent):
    array = Pila()
    balanced = True
    index = 0
    while index < len(array_parent) and balanced:
        for value in array_parent:
            #Para corchetes abiertos
            if value == '(':
                array.push(value)
            elif value == ')':
                if array.empty():
                    balanced = False
                else:
                    array.pop()
            #Para corchetes cerrados
            if value == '[':
                array.push(value)
            elif value == ']':
                if array.empty():
                    balanced = False
                else:
                    array.pop()
        index += 1
    if balanced and array.empty():
        return True
    else:
        return False



def main():
    tries = int(stdin.readline().strip())
    while tries != 0:
        parenthesis = list(map(str, stdin.readline().strip()))
        answer = balanced(parenthesis)
        if answer:
            print('Yes')
        elif not answer:
            print('No')
        tries -= 1

main()