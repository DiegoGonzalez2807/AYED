#Diego Alejandro Gonzalez Gualteros
#2163199
#1007196603
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

class Cola:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def updateHead(self,new_value):
        self.head = new_value

    def updateTail(self,new_value):
        self.tail = new_value

    def empty(self):
        if self.tail == self.head and self.getHead() is None:
            return True
        else:
            return False

    def enqueue(self,value):
        tail = self.getTail()
        new_value = Node(value)
        if isinstance(new_value, Node) and self.empty():
            self.updateHead(new_value)
            self.updateTail(new_value)
            self.len += 1
        elif isinstance(new_value, Node) and not self.empty():
            new_value.updatebefore(tail)
            tail.updateafter(new_value)
            self.updateTail(new_value)
            self.len += 1

    def dequeue(self):
        head,tail = self.getHead(), self.getTail()
        if len(self) == 1:
            self.updateHead(None)
            self.updateTail(None)
            self.len -= 1
            return head.getData()
        if not self.empty():
            head.getAfter().updatebefore(None)
            self.updateHead(head.getAfter())
            head.updateafter(None)
            self.len -=1
            return head.getData()



def main():
    cases = int(stdin.readline().strip())
    cola = Cola()
    for case in range(cases):
        instru = int(stdin.readline().strip())
        for i in range(instru):
            in1 = str(stdin.readline().strip())
            if in1 == 'Siguiente':
                if cola.empty():
                    print('No hay fila')
                else:
                    print(cola.dequeue())
            else:
                cola.enqueue(in1)


main()

