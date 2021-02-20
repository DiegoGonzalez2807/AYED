from sys import stdin
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def __len__(self):
        return self.len

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        node = Node(item)
        node.setNext(self.head)
        if self.head is not None:
            self.head.setPrev(node)
        self.head = node
        self.len += 1

    def printList(self):
        current = self.head
        while current != None:
            if current.getData() is not None:
                print(current.getData())

            current = current.getNext()

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData()[0] == item:
                found = True
            else:
                current = current.getNext()

        return found, current.getData()[1]

    def getHead(self):
        return self.head

    def remove(self, item):
        try:
            current = self.head
            found = False
            while current != None and not found:
                if current.getData() == item:
                    found = True
                else:
                    current = current.getNext()

            if current.getPrev() == None:
                current.setNext(None)
                self.head = current.getNext()
                self.head.setPrev(None)
            else:
                current.getPrev().setNext(current.getNext())
                current.setPrev(None)
                current.setNext(None)
            self.len -= 1
        except:
            return -1


    def take_maximum(self):
        head = self.gethead()
        max_number, current = head, head
        if not self.isEmpty():
            while current is not None:
                if max_number.getData() < current.getData():
                    max_number = current
                current = current.getNext()
        self.remove(max_number)
        return max_number.getData()

def main():
    cases = int(stdin.readline().strip())
    cola = LinkedList()
    for case in range(cases):
        instruction = list(map(str,stdin.readline().strip().split()))
        if instruction[0] == 'inserte':
            cola.add(int(instruction[1]))
        elif instruction[0] == 'saque' and not cola.isEmpty():
            print(cola.take_maximum())
main()
