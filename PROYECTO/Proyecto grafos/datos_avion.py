from sys import stdin
class HashTable:
    def __init__(self, size):
        self.elements = [ [] for x in range(size) ]
        self.keys = set()

    def search(self, key):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key :
                return e[1]
        return None

    def assign(self, index, element):
        self.elements[index].append(element)

    def getElements(self):
        return self.elements

    def getKeys(self):
        return self.keys

    def printHashTable(self):
        print('========== Hash Table Composition ================')
        print('Elements')
        for index in range(len(self.elements)):
            print(index, ':', self.elements[index])
        print('Keys', self.keys)

    def insert(self, key, element):
        index = self.hash(key)
        self.position(index, key, element)
        self.keys.add(key)

    def hash(self, key):
        return hash(key) % len(self.elements)

    def position(self, key, element, index):
        if self.elements[index] != None:
            print('El pasajero', self.elements[index][1], 'Ya confirmó su vuelo? Si No')
            ans1 = stdin.readline().strip()
            if ans1.capitalize() == 'Si':
                return self.position(key, element, self.hash(index))
            elif ans1.capitalize() == 'No':
                self.assign(index, (key,element))
        elif self.elements[index] == None:
            self.assign(index,(key,element))

    def review(self):
        answer = False
        for value in self.elements:
            if self.elements[value] == None:
                answer = True
        return answer


