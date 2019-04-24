from BinaryTree import *

def depthFirstSearch(bt, value):
    if (bt.root == None):
        return None
    else:
        l = list()
        return depthSearch(bt.root, value, l)

def depthSearch(node, value, l = list()):
    if (node.value in l):
        return
    l.append(node.value) #keep track of nodes being checked, in case of graph
    print("checking "+str(node.value))
    if (node.value ==value):
        return True
    if (node.right != None and node.left != None):
        if (depthSearch(node.left, value, l) == True or depthSearch(node.right, value, l) == True):
            return True
    elif (node.left != None):
        if (node.left.value not in l):
            return depthSearch(node.left, value, l)
    elif (node.right != None):
        if (node.right.value not in l):
            return depthSearch(node.right, value, l)
    return False

binaryTree = BinaryTree()
binaryTree.insert("A")
binaryTree.insert("B")
binaryTree.insert("C")
binaryTree.insert("D")
binaryTree.insert("E")
binaryTree.insert("F")
binaryTree.insert("G")
print(binaryTree.printInOrder())
print(depthFirstSearch(binaryTree, "E"))
print(depthFirstSearch(binaryTree, "G"))
