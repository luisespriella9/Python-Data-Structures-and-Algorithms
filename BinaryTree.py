'''
Code to implement a Binary Tree
'''
from queue import*

class BinaryNode():
    value = None
    left = None
    right = None

class BinaryTree():
    root = None
    #initializing binary tree
    
    def _init_(self):
        self.root = None
    
    def printInOrder(self):
        l = list()
        return self.inOrder(node = self.root, l = l)
    
    def inOrder(self, node, l):
        if (node.left != None):
            self.inOrder(node.left, l)
        l.append(node.value)
        if (node.right != None):
            self.inOrder(node.right, l)
        return l
    
    def insert(self, value):
        #insert into binary tree
        if (self.root == None):
            temporaryNode = BinaryNode()
            temporaryNode.value = value
            self.root = temporaryNode
        else:
            self.insertValue(self.root, value)
    '''
        since we are inserting always at the left most end we will have to use a queue and do breadth first search to explore from left to right at the same level
        '''
    def insertValue(self, node, value):
        nodeToInsert = BinaryNode()
        nodeToInsert.value = value
        queue = Queue()
        queue.enqueue(node)
        while (not queue.isEmpty()):
            tempNode = queue.dequeue()
            if (tempNode.value.left == None):
                tempNode.value.left = nodeToInsert
                return tempNode
            elif (tempNode.value.right == None):
                tempNode.value.right = nodeToInsert
                return tempNode
            queue.enqueue(tempNode.value.left)
            queue.enqueue(tempNode.value.right)

    def checkIfBST(self):
        #hard for it to be a BST since it must also be a complete binary tree and somehow all elements had to be added in the perfect way since a binary adds from left to right from level to level
        return self.BST(node = self.root)
    
    def BST(self, node, minimum = None, maximum=None):
        if (minimum == None and maximum != None):
            if (node.value > maximum):
                return False
        elif (minimum != None and maximum == None):
            if (node.value < minimum):
                return False
        elif (minimum != None and maximum != None):
            if (node.value < minimum or node.value > maximum):
                return False
        #do nothing if both equal none, aka root whose min and max should be none
        if (node.left != None and node.right != None):
            if (self.BST(node.left, minimum, node.value) == False or self.BST(node.right, node.value, maximum) == False):
                return False
            else:
                return True
        if (node.left != None):
            self.BST(node.left, minimum, node.value)
        #max is now its root
        if (node.right != None):
            self.BST(node.right, node.value, maximum)
        return True


if __name__ == "__main__":
    print("running main")
    tree = BinaryTree()
    print("lets check for a not BST")
    tree.insert(8)
    tree.insert(20)
    tree.insert(30)
    tree.insert(5)
    tree.insert(80)
    tree.insert(70)
    tree.insert(3)
    tree.insert(1)
    print(tree.printInOrder())
    print(tree.checkIfBST())
    
    print("lets check for a BST")
    tree1 = BinaryTree()
    tree1.insert(8)
    tree1.insert(6)
    tree1.insert(12)
    tree1.insert(3)
    tree1.insert(7)
    tree1.insert(10)
    tree1.insert(15)
    print(tree1.printInOrder())
    print(tree1.checkIfBST())

