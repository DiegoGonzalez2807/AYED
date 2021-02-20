from DoubleLinkedList import Node

class LinkedStack:
    def __init__(self):
        self.top = None
        self.len = 0

    def __len__(self):
        return self.len

    def getTop(self):
        return self.top

    def _setTop(self,element):
        self.top = element

    def isEmpty(self):
        return True if self.top is None else False

    def Push(self, item):
        Top = self.getTop()
        element = Node(item)
        if isinstance(element, Node) and self.isEmpty():
            self._setTop(element)
            self.len += 1
        elif isinstance(element, Node):
            element.setPrev(Top)
            Top.setNext(element)
            self._setTop(element)
            self.len += 1

    def Pop(self):
        if not self.isEmpty():
            get = self.getTop()
            self._setTop(get.getPrev())      #set actualizar
            get.setPrev(None)                #get pedir
            self.getTop().setNext(None)
            self.len -= 1
            return get.getData()

    def printStack(self):
        current = self.top
        while current != None:
            if current.getData() is not None:
                print(current.getData())

            current = current.getNext()

class LinkedQueue:
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

    def _setTail(self,element):
        self.tail = element

    def _setHead(self,element):
        self.head = element

    def isEmpty(self):
        return True if self.tail == self.head else False

    def Enqueue(self,item):
        Tail = self.tail
        element = Node(item)
        if isinstance(element,Node) and not self.isEmpety():
            element.setNext(Tail)
            Tail.setPrev(element)
            self._setTail(element)
            self.len += 1
        elif isinstance(element,Node):
            self._setHead(element)
            self.len += 1


    def Dequeue(self):
        Head, Tail = self.head, self.tail       #set actualizar
        if not self.isEmpety():                 #get pedir
            Head.setPrev(None)
            Head.getPrev().setNext(None)
            self._setHead(Head.getPrev())
            self.len -= 1

    def printQueue(self):
        current = self.head
        while current != None:
            if current.getData() is not None:
                print(current.getData())

            current = current.getNext()
