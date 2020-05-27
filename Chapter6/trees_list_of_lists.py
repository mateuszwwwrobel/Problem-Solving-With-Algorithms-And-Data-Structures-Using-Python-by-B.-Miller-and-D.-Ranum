



#myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
#print(myTree)
#print('left subtree = ', myTree[1])
#print('root = ', myTree[0])
#print('right subtree = ', myTree[2])


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t)>1:
        root.insert(1, [newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root


def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]




r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
#print(l)

rt=getRightChild(r)
#print(rt)
setRootVal(l,9)
#print(r)
insertLeft(l,11)
#print(r)
#print(getRightChild(r))
#print(getRightChild(getRightChild(r)))



x = BinaryTree('a')

insertLeft(x, "b")
insertRight(x, "c")
insertLeft(getRightChild(x),'d')

insertRight(getRightChild(x),'f')
insertRight(getLeftChild(x),'e')

print(x[0])
print(x[1])
print(x[2])
print(x)




def buildTree():
    pass

ttree = buildTree()
getRootVal(getRightChild(ttree),'c')
getRootVal(getRightChild(getLeftChild(ttree)),'d')
getRootVal(getRightChild(getRightChild(ttree)),'f')

print(ttree)