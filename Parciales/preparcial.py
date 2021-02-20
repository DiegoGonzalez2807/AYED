#Preparcial
#Diego Gonzalez
#8/10/2020
from sys import stdin
class Node:
    def __init__(self, user, priority):
        self.before = None
        self.after = None
        self.user = user
        self.priority = priority

    def getUser(self):
        return self.user

    def getBefore(self):
        return self.before

    def getAfter(self):
        return self.after

    def getPriority(self):
        return self.priority

    def updatebefore(self, newdata):
        self.before = newdata

    def updateafter(self, newdata):
        self.after = newdata

    def updateuser(self, newdata):
        self.user = newdata

    def updatepriority(self,newdata):
        self.priority = newdata



class Cola:
    def __init__(self):
        self.head = None
        self.tail = None

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def updateHead(self, new_value):
        self.head = new_value

    def updateTail(self, new_value):
        self.tail = new_value

    def empty(self):
        if self.tail == self.head and self.getHead() is None:
            return True
        else:
            return False

    def enqueue(self, user,priority):
        tail = self.getTail()
        new_value = Node(user,priority)
        if isinstance(new_value, Node) and self.empty():
            self.updateHead(new_value)
            self.updateTail(new_value)
        elif isinstance(new_value, Node) and not self.empty():
            new_value.updatebefore(tail)
            tail.updateafter(new_value)
            self.updateTail(new_value)

    def dequeue(self):
        head = self.getHead()
        tail = self.getTail()
        max_priority = head
        current = head
        if not self.empty():
            while current is not None:
                #Primero revisar la prioridad mas grande
                if max_priority.getPriority() < current.getPriority():
                    max_priority = current
                current = current.getAfter()
            #Primero se imprime la persona con mayor prioridad
            if max_priority.getUser() == head.getUser():
                print('Persona con mayor prioridad', head.getUser)
                print('Prioridad:', max_priority.getPriority())
            #Ahora se elimina
                head.getAfter().updatebefore(None)
                self.updateHead(head.getAfter())
                head.updateafter(None)
            #mirar si la max_priority es la mas grande
            if max_priority.getPriority() > current.getPriority():
                if max_priority.getAfter() is not None:
                    max_priority.getAfter().updateafter(max_priority.getBefore())

    def printList(self):
        current = self.head
        while current != None:
            if current.getData() is not None:
                print(current.getData())
            current = current.getAfter()


def main():
    line = stdin.readline().strip().split()
    cola = Cola()
    while line:
        if len(line) == 1:
            print('Usuario no valido')
        else:
            user = line[0]
            priority = int(line[1])
            cola.enqueue(user,priority)
            print('Ingresar usuario')



main()
