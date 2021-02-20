#Diego Alejandro Gonzalez Gualteros
#2163199
#1007196603
from sys import stdin
class BinaryTree:
    def __init__(self, treeValue=None):
        self.root = treeValue
        self.left = None
        self.right = None

    #Setters
    def getRoot(self):
        return self.root

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRoot(self, root):
        self.root = root

    def setRight(self, right):
        if isinstance(right, BinaryTree):
            self.right = right

    def setLeft(self, left):
        if isinstance(left, BinaryTree):
            self.left = left

    def insertManyBST(self, values):
        for value in values:
            self.insertValueBST(value)

    def insertValueBST(self, value):
        left, right = self.getLeft(), self.getRight()
        if self.root is None:
            self.setRoot(value)
        else:
            if value >= self.root:
                # Si no hay árbol a la derecha
                if right is None:
                    self.setRight(BinaryTree(value))
                else:
                    # Si hay árbol a la derecha
                    right.insertValueBST(value)
            if value < self.root:
                if left is None:
                    self.setLeft(BinaryTree(value))
                else:
                    # Si hay árbol a la derecha
                    left.insertValueBST(value)


    def searchBST(self, value):
        left, right = self.getLeft(), self.getRight()
        if value < self.root and left is not None:
            return left.searchBST(value)
        elif value > self.root and right is not None:
            return right.searchBST(value)
        return self.root if self.root == value else None

    def MinimumTree(self):
        current = self
        while self.getLeft() is not None:
            current = current.getLeft()
        return current

    def MaximumTree(self):
        current = self
        while self.getRight() is not None:
            current = current.getRight()
        return current

    def printRoot(self):
        print(self.root)

    def inOrder(self):
        left, right = self.getLeft(), self.getRight()
        # Izquierda - Raiz - Derecha
        if left is not None:
            left.inOrder()
        self.printRoot()
        if right is not None:
            right.inOrder()

    def preOrder(self):
        # Raiz - Izquierda - Derecha
        left, right = self.getLeft(), self.getRight()
        self.printRoot()
        if left is not None:
            left.preOrder()
        if right is not None:
            right.preOrder()

    def posOrder(self):
        # Izquierda - Derecha - Raíz
        left, right = self.getLeft(), self.getRight()
        if left is not None:
            left.posOrder()
        if right is not None:
            right.posOrder()


def recons(orderpre, orderin):
    if orderin == []:
        return None
    preor = BinaryTree(orderpre[0])
    index = orderin.index(preor.root)
    inright = orderin[index+1:]
    inleft = orderin[:index]
    preor.setRight(recons(orderpre[len(inleft) + 1:], inright))
    preor.setLeft(recons(orderpre[1:len(inleft) + 1], inleft))
    return preor

def printer(self):
    if self is None:
        return ''
    else:
        return printer(self.getLeft()) + printer(self.getRight()) + str(self.getRoot())



def main():
    line = stdin.readline().strip()
    while line:
        preor,inor = line.split()
        inor = list(inor)
        preor = list(preor)
        tree = recons(preor,inor)
        print(printer(tree))
        line = stdin.readline().strip()
main()