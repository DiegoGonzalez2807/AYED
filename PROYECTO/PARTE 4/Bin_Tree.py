class BinaryTree:
    def __init__(self, treeValue=None):
        self.root = treeValue
        self.left = None
        self.right = None

    def __str__(self):
        return 'T('+str(self.root)+')'

    #Setters
    def setRoot(self, root):
        self.root = root

    def _setRight(self, right):
        if isinstance(right, BinaryTree):
            self.right = right

    def _setLeft(self, left):
        if isinstance(left, BinaryTree):
            self.left = left

    def insertManyBST(self, values):
        for value in values:
            self.insertValueBST(value)

    def insertValueBST(self, value):
        left, right = self.getLeft(), self.getRight()
        if self.root is None :
            self.setRoot(value)
        else:
            if value >= self.root:
                # Si no hay árbol a la derecha
                if right is None :
                    self._setRight(BinaryTree(value))
                else:
                    #Si hay árbol a la derecha
                    right.insertValueBST(value)
            if value < self.root:
                if left is None :
                    self._setLeft(BinaryTree(value))
                else:
                    #Si hay árbol a la derecha
                    left.insertValueBST(value)

    def searchBST(self, value):
        left, right = self.getLeft(), self.getRight()
        if value < self.root[0] and left is not None:
            return left.searchBST(value)
        elif value > self.root[0] and right is not None:
            return right.searchBST(value)
        return self.root[1] if self.root[0] == value else None

    def getRoot(self):
        return self.root

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def printRoot(self):
        print(self.root)

    def inOrder(self):
        left, right = self.getLeft(), self.getRight()
        #Izquierda - Raiz - Derecha
        if left is not None:
            left.inOrder()
        self.printRoot()
        if right is not None:
            right.inOrder()

    def preOrder(self):
        #Raiz - Izquierda - Derecha
        left, right = self.getLeft(), self.getRight()
        self.printRoot()
        if left is not None:
            left.preOrder()
        if right is not None:
            right.preOrder()

    def posOrder(self):
        #Izquierda - Derecha - Raíz
        left, right = self.getLeft(), self.getRight()
        if left is not None:
            left.posOrder()
        if right is not None:
            right.posOrder()
        self.printRoot()