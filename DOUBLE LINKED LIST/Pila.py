#Diego Alejandro Gonzalez Gualteros
#2163199
#1007196603
from sys import stdin
class Node:
    def __init__(self, initial_data):
        self.before = None
        self.after = None
        self.data = initial_data
        self.len = 0

    def __len__(self):
        return self.len

    def getData(self):
        return self.data

    def getBefore(self):
        return self.before

    def getAfter(self):
        return self.after

    def updatebefore(self, newdata):
        self.before = newdata

    def updateafter(self, newdata):
        self.after = newdata

    def updatedata(self, newdata):
        self.data = newdata

class Pila:
    def __init__(self):
        self.index = None
        self.len = 0

    def __len__(self):
        return self.len

    def getIndex(self):
        return self.index

    def updateIndex(self, newvalue):
        self.index = newvalue

    def empty(self):
        return len(self) == 0

    def push(self, value):
        index = self.getIndex()
        new_value = Node(value)
        if isinstance(new_value, Node) and self.empty():
            self.updateIndex(new_value)
            self.len += 1
        elif isinstance(new_value, Node) and not self.empty():
            new_value.updatebefore(index)
            index.updateafter(new_value)
            self.updateIndex(new_value)
            self.len += 1
        return value

    def pop(self):
        if not self.empty():
            index = self.getIndex()
            self.updateIndex(index.getBefore())
            index.updatebefore(None)
            self.getIndex().updateafter(None)
            self.len -= 1
            return index.getData()

    def printList(self):
        current = self.index
        while current != None:
            if current.getData() is not None:
                print(current.getData())
            current = current.getBefore()


def balanced(array_parent):
    array = Pila()
    balanced = True
    index = 0
    while index < len(array_parent)-1 and balanced:
        for value in array_parent:
            # Para corchetes abiertos
            if value == '(':
                print('Este se inserta',array.push(value))
                print('Esta es la lista', array.printList())
            elif value == ')':
                if array.empty():
                    balanced = False
                else:
                    print('Este se elimina',array.pop())
                    print('Esta es la lista', array.printList())

            # Para corchetes cerrados
            if value == '[':
                print('Este se inserta',array.push(value))
                print('Esta es la lista', array.printList())
            elif value == ']':
                if array.empty():
                    balanced = False
                else:
                    print('Este se elimina',array.pop())
                    print('Esta es la lista', array.printList())
        index += 1
    if balanced and array.empty():
        return True
    else:
        return False


def main():
    tries = int(stdin.readline().strip())
    while tries != 0:
        parenthesis = list(map(str, stdin.readline().strip()))
        print(parenthesis)
        answer = balanced(parenthesis)
        if answer:
            print('Yes')
        else:
            print('No')
        tries -= 1

main()

