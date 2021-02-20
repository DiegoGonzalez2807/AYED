from sys import stdin
from random import randint
import Bin_Tree
import Double_Linked_List
import Heaps

#Alberto Naranjo AYED-1
#Diego Gonzalez AYED-2

RANDOM_NUMBERS = 200
RANDOM_SEED = 500
HASH_TABLE_SIZE = 57


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

    def insert(self, key,element):
        index = self.hash(key)
        self.assign(index, (key,element))
        self.keys.add(key)
        print(element, 'has been assigned with key', key, 'on index', index)

    def hash(self, key):
        return hash(key) % len(self.elements)



class Linked_Hash:
    def __init__(self, size):
        self.elements = [ Double_Linked_List.DLinkedList() for x in range(size) ]
        self.keys = set()

    def search(self, key):
        index = self.hash(key)
        flag,Value = self.elements[index].search(key)
        if flag:
            return Value
        return None

    def assign(self, index, element):
        self.elements[index].add(element)

    def getElements(self):
        return self.elements

    def getKeys(self):
        return self.keys

    def printHashTable(self):
        print('========== Hash Table Composition ================')
        print('Elements')
        for index in range(len(self.elements)):
            print(index, ':', self.elements[index].printList())
        print('Keys', self.keys)

    def insert(self, key,element):
        index = self.hash(key)
        self.assign(index, (key,element))
        self.keys.add(key)
        print(element, 'has been assigned with key', key, 'on index', index)

    def hash(self, key):
        return hash(key) % len(self.elements)

class Binary_Hash:
    def __init__(self, size):
        self.elements = [ Bin_Tree.BinaryTree() for x in range(size) ]
        self.keys = set()

    def search(self, key):
        index = self.hash(key)
        value = self.elements[index].searchBST(key)
        return value

    def assign(self, index, element):
        self.elements[index].insertValueBST(element)

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

    def insert(self, key,element):
        index = self.hash(key)
        self.assign(index, (key,element))
        self.keys.add(key)
        print(element, 'has been assigned with key', key, 'on index', index)

    def hash(self, key):
        return hash(key) % len(self.elements)

class Heaps_Hash:
    def __init__(self, size):
        self.elements = [ Heaps.PriorityQueue([],'Max') for x in range(size) ]
        self.keys = set()

    def search(self, key):
        index = self.hash(key)
        list = self.elements[index].getHeap().copy().HeapSort()
        ret = binary_search(list, key)
        return list[ret][1] if ret is not None else None


    def assign(self, index, element):
        self.elements[index].enqueue(element)

    def getElements(self):
        return self.elements

    def getKeys(self):
        return self.keys

    def printHashTable(self):
        print('========== Hash Table Composition ================')
        print('Elements')
        for index in range(len(self.elements)):
            print(index, ':', self.elements[index].printElements())
        print('Keys', self.keys)

    def insert(self, key,element):
        index = self.hash(key)
        self.assign(index, (key, element))
        self.keys.add(key)
        print(element, 'has been assigned with key', key, 'on index', index)

    def hash(self, key):
        return hash(key) % len(self.elements)

def binary_search(A, k):
    low = 0
    high = len(A)
    while low < high:
        mid = low + (high - low) // 2
        if A[mid][0] == k:
            return mid
        else:
            if A[mid][0] > k:
                high = mid
            else:
                low = mid + 1
