from BinaryTree import *

def breadthFirstSearch(bt, value):
    if (bt.root == None):
        return None
    else:
        l = list()
        return breadthSearch(bt.root, value, l)

def breadthSearch(root, value, l = list()):
    queue = Queue()
    queue.enqueue(root)
    while (not queue.isEmpty()):
        node = queue.dequeue().value
        print("checking "+str(node.value))
        if (node.value == value):
            return True
        if (node.left != None):
            if (node.left.value not in l):
                queue.enqueue(node.left)
        if (node.right != None):
            if (node.right not in l):
                queue.enqueue(node.right)
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
print(breadthFirstSearch(binaryTree, "E"))
print(breadthFirstSearch(binaryTree, "G"))
