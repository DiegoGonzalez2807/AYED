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

class DLinkedList:
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