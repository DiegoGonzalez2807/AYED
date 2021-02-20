from sys import stdin
def main():
    cases = int(stdin.readline().strip())
    for case in range(cases):
        wagons = int(stdin.readline().strip())
        train = list(map(int,stdin.readline().strip().split()))
        cont = 0
        for i in range(wagons):
            for j in range(i+1,wagons):
                if train[i] > train[j]:
                    train[i] , train[j] = train[j] , train[i]
                    cont += 1
        print('Optimal train swapping takes', cont, 'swaps.')
main()



















from sys import stdin
class Node:
    def __init__(self, initial_data):
        self.before = None
        self.after = None
        self.data = initial_data

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
        return self.index == None

    def Push(self, value):
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

    def Pop(self):
        if not self.empty():
            index = self.getIndex()
            self.updateIndex(index.getBefore())
            index.updatebefore(None)
            self.getIndex().updateafter(None)
            self.len -= 1
            return index.getData()

def balanced(array_parent):
    array = Pila()
    #Balanced empieza en True pues es una de las reglas de que si esta vacia, entonces es valida
    balanced = True
    index = 0
    #Mientras que no se haya llegado a la ultima posicion del arreglo y aun se vea que puede estar balanceado
    while index < len(array_parent) and balanced:
        parent_1 = array_parent[index]
        if parent_1 == '(' or parent_1 == '[':
            array.Push(parent_1)
        elif parent_1 == ')' or parent_1 == ']':
            #Si se empezo con un derecho
            if array.empty():
                balanced = False
            else:
                array.Pop()
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
        print(balanced(parenthesis))
main()