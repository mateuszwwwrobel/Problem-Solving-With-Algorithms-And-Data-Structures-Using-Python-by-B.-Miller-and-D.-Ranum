

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, NewNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(NewNode)
        else:
            t = BinaryTree(NewNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, NewNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(NewNode)
        else:
            t = BinaryTree(NewNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key




def main():
    x = BinaryTree('a')
    x.insertLeft('b')
    x.insertRight('c')
    x.getLeftChild().insertRight('d')

    x.getRightChild().insertLeft('e')
    x.getRightChild().insertRight('f')

    print(x.getRightChild().getRightChild().getRootVal())
    return print(x)

    

main()

