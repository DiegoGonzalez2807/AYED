from sys import stdin
class Node:
    def __init__(self, user):
        self.before = None
        self.after = None
        self.user = user

    def getUser(self):
        return self.user

    def getBefore(self):
        return self.before

    def getAfter(self):
        return self.after

    def updatebefore(self, newdata):
        self.before = newdata

    def updateafter(self, newdata):
        self.after = newdata

    def updateuser(self, newdata):
        self.user = newdata

class Cola:
    def __init__(self):
        self.head = None
        self.tail = None

    def getHead(self):
        return self.head

    def updateHead(self,newvalue):
        self.head = newvalue

    def getTail(self):
        return self.tail

    def updateTail(self,newvalue):
        self.tail = newvalue

    def empty(self):
        if self.head == self.tail and self.getHead() is None:
            return True
        else:
            return False

    def enqueue(self,newvalue):
        tail = self.tail
        new = Node(newvalue)
        if not self.empty():
            new.updatebefore(tail)
            tail.updateafter(new)
            self.updateTail(new)
        else:
            self.updateHead(new)
            self.updateTail(new)

    def dequeue(self):
        head = self.getHead()
        maximum,current = head,head
        if not self.empty():
            while current is not None:
                if maximum.getUser() < current.getUser():
                    maximum = current
                current = current.getAfter()
            print(maximum)
            if maximum.getUser() == head.getUser():
                print(head.getUser())
            head.getAfter().updatebefore(None)
            self.updateHead(head.getAfter())
            head.updateafter(None)
        elif self.empty():
            print('')

    def printList(self):
        current = self.head
        while current != None:
            if current.getUser() is not None:
                print(current.getUser())
            current = current.getAfter()

def main():
    cola = Cola()
    tries = int(stdin.readline().strip())
    for line in range(tries):
        order = stdin.readline().strip().split()
        if 'inserte' in order:
            cola.enqueue(order[1])
            cola.printList()
        elif 'saque' and 'máximo' in order:
            if not cola.empty():
                print(cola.dequeue())
main()