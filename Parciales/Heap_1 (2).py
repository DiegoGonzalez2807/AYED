import math
from sys import stdin

class PriorityQueue:
    def __init__(self, A,propertyCheck=0):
        self.heap = Heap(A, propertyCheck)

    def printElements(self):
        for e in self.heap.getElements():
            print(e)

    def getElements(self):
        return self.elements

    def getHeap(self):
        return self.heap

    def enqueue(self, element):
        self.heap.insert(element)

    def dequeue(self):
        first_element = self.heap.elements[0]
        self.heap.delete(first_element)
        return first_element

    def __len__(self):
        return len(self.heap.getElements())

class Heap:
    def __init__(self, A, propertyCheck=0):
        self.elements = []
        self.propertyCheck = propertyCheck
        for e in A:
            self.insert(e)

    def __str__(self):
        return str(self.elements)

    def getElements(self):
        return self.elements

    def parent(self, i):
        return (i//2 - 1 ) if i%2 == 0 else i//2

    def right(self, i):
        return 2*(i+1)

    def left(self, i):
        return 2*i + 1

    def height(self):
        return math.ceil(math.log(len(self.elements),2))

    def buildMaxHeap(self):
        for i in range(len(self.elements)//2 + 1, -1, -1):
            self.maxHeapify(i)

    def insert(self, element):
        self.elements.append(element)
        self.buildMaxHeap()

    def delete(self, key):
        self.elements.remove(key)
        self.buildMaxHeap()

    def update(self, key, new_key):
        self.delete(key)
        self.insert(new_key)

    def maxHeapify(self,root):
        #Identificar los elementos del árbol
        left = self.left(root)
        right = self.right(root)
        length = len(self.elements)
        propertyCheck = self.propertyCheck
        #Determinar índice en donde se incumple la regla de maximalidad
        largest = left if left < length and self.elements[root][propertyCheck] < self.elements[left][propertyCheck] else root
        if right < length and self.elements[largest][propertyCheck] < self.elements[right][propertyCheck]:
            largest = right
        # Realizar la actualización del árbol corrigiendo las posiciones
        if largest != root:
            self.elements[largest], self.elements[root] = self.elements[root], self.elements[largest]
            #Propagar el invariante hacia arriba
            self.maxHeapify(largest)

    def heapsort(self):
        array = []
        for i in self.elements:
            array.append(i)
            self.delete(i)
        return array


def main():
    line = list(map(int,stdin.readline().strip().split()))
    length_queue, my_work = line[0], line[1]
    priorities = list(map(int,stdin.readline().strip().split()))
    p2 = PriorityQueue(priorities,0)
    print(p2)
    while len(p2) > 0:
        print('siguiente a atender', p2.dequeue())
main()