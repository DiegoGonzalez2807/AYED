class PriorityQueue:
    def __init__(self, A, Operation, propertyCheck = 0):
        self.op = Operation
        if Operation.capitalize() == 'Max':
            self.heap = MaxHeap(A, propertyCheck)
        elif Operation.capitalize() == 'Min':
            self.heap = MinHeap(A, propertyCheck)

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

class MaxHeap:
    def __init__(self, A, propertyCheck=0):
        self.elements = []
        self.propertyCheck = propertyCheck
        for e in A:
            self.insert(e)

    def __str__(self):
        return str(self.elements)

    def getElements(self):
        return self.elements

    def copy(self):
        return MaxHeap(self.elements, self.propertyCheck)

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

    def buildMinHeap(self):
        for i in range(len(self.elements) // 2 + 1, -1, -1):
            self.minHeapify(i)

    def insert(self, element):
        self.elements.append(element)
        self.buildMaxHeap()
        print(self.elements )

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

    def HeapSort(self):
        ret = []
        for i in self.elements:
            ret.append(i)
            self.delete(i)
        return ret

class MinHeap:
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

    def buildMinHeap(self):
        for i in range(len(self.elements) // 2 + 1, -1, -1):
            self.minHeapify(i)

    def insert(self, element):
        self.elements.append(element)
        self.buildMinHeap()

    def delete(self, key):
        self.elements.remove(key)
        self.buildMinHeap()

    def update(self, key, new_key):
        self.delete(key)
        self.insert(new_key)

    def minHeapify(self,root):
        #Identificar los elementos del árbol
        left = self.left(root)
        right = self.right(root)
        length = len(self.elements)
        propertyCheck = self.propertyCheck
        #Determinar índice en donde se incumple la regla de maximalidad
        largest = left if left < length and self.elements[root][propertyCheck] > self.elements[left][propertyCheck] else root
        if right < length and self.elements[largest][propertyCheck] > self.elements[right][propertyCheck]:
            largest = right
        # Realizar la actualización del árbol corrigiendo las posiciones
        if largest != root:
            self.elements[largest], self.elements[root] = self.elements[root], self.elements[largest]
            #Propagar el invariante hacia arriba
            self.minHeapify(largest)

    def HeapSort(self):
        ret = []
        for i in self.elements:
            ret.append(i)
            self.delete(i)
        return ret