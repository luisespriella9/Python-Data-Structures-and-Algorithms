'''
Code to implement a binary search tree
'''

class BinaryNode():
    value = None
    left = None
    right = None

class BinarySearchTree():
    root = None
    #initializing Binary search tree
    def _init_(self):
        self.root = None
    
    def insert(self, value):
        if (self.root == None):
            self.root = BinaryNode()
            self.root.value = value
        else:
            self.insertValue(self.root, value)
    
    def insertValue(self, node, value):
        #recursive
        if (value < node.value):
            if (node.left == None):
                node.left = BinaryNode()
                node.left.value = value
                return
            else:
                self.insertValue(node.left, value)
        elif (value > node.value):
            if (node.right == None):
                node.right = BinaryNode()
                node.right.value = value
                return
            else:
                self.insertValue(node.right, value)
    
    #prints the tree in order
    # left, root, right
    #prints this as a list
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
    
    def find(self, value):
        return self.findValue(self.root, value)
    
    def findValue(self, node, value):
        if (node.value == value):
            return True
        if (node.left != None and value < node.value):
            return self.findValue(node.left, value)
        if (node.right != None and value > node.value):
            return self.findValue(node.right, value)
        return False
    
    #finds min of tree or subtree
    def findMin(self, node):
        if (node.left == None):
            return node
        else:
            return self.findMin(node.left)
    
    def delete(self, value):
        if (self.root.value == value):
            temporaryNode = self.findMin(self.root.right)
            deleteValue(temporaryNode)
            self.root = temporaryNode
        else:
            if (self.find(value)):
                self.deleteValue(self.root, value)
    
    #keep track of parent
    def deleteValue(self, node, value):
        #base cases
        #leaf, aka no children
        if (node.value == value):
            if (node.left == None and node.right == None):
                return None
            #one children at the left
            elif (node.left != None and node.right == None):
                return node.left
            #one children at the right
            elif (node.left == None and node.right != None):
                return node.right
            else:
                #two children
                temporaryNode = BinaryNode()
                temporaryNode.value = self.findMin(node.right).value
                temporaryNode.left = node.left
                temporaryNode.right = node.right
                self.delete(temporaryNode.value)
                return temporaryNode
        if (value < node.value):
            if (node.left != None):
                if (node.left.value == value):
                    node.left = self.deleteValue(node.left, value)
                else:
                    self.deleteValue(node.left, value)
        elif (value > node.value):
            if (node.right != None):
                if (node.right.value == value):
                    node.right = self.deleteValue(node.right, value)
                else:
                    self.deleteValue(node.right, value)


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(8)
    tree.insert(6)
    tree.insert(12)
    tree.insert(3)
    tree.insert(7)
    tree.insert(10)
    tree.insert(15)
    tree.insert(9)
    tree.insert(13)
    tree.insert(17)
    tree.insert(16)
    tree.insert(18)
    print(tree.printInOrder())
    print(tree.find(15)) #True
    print(tree.find(6)) #True
    print(tree.find(2)) #False
    tree.delete(15)
    print(tree.printInOrder())
