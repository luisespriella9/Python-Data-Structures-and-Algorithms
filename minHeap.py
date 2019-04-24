from queue import *
class HeapNode():
    parent = None
    value = None
    left = None
    right = None

class MinHeap():
    root = None
    def insert(self, value):
        #insert into binary tree
        if (self.root == None):
            temporaryNode = HeapNode()
            temporaryNode.value = value
            self.root = temporaryNode
        else:
            node = self.insertValue(self.root, value)
            self.maintainStructure(node)

    def insertValue(self, node, value):
        nodeToInsert = HeapNode()
        nodeToInsert.value = value
        queue = Queue()
        queue.enqueue(node)
        while (not queue.isEmpty()):
            tempNode = queue.dequeue()
            if (tempNode.value.left == None):
                tempNode.value.left = nodeToInsert
                nodeToInsert.parent = tempNode.value
                return nodeToInsert
            elif (tempNode.value.right == None):
                tempNode.value.right = nodeToInsert
                nodeToInsert.parent = tempNode.value
                return nodeToInsert
            queue.enqueue(tempNode.value.left)
            queue.enqueue(tempNode.value.right)

    def maintainStructure(self, node):
        print(node.value)
        while (node.parent != None ):
            if (node.parent.value > node.value):
                if (node.parent!=self.root):
                    self.switch(node.parent, node)
                else:
                    if (self.root.left == node):
                        node.parent.left = node.left
                        temp = node.parent.right
                        node.parent.right = node.right
                        node.right = temp
                        node.left = node.parent
                        self.root = node
                        return
                    elif (self.root.right == node):
                        node.parent.right = node.right
                        temp = node.parent.left
                        node.parent.left = node.left
                        node.left = temp
                        node.right = node.parent
                        self.root = node
                        return
            else:
                break

    def switch(self, parent, node):
        if (parent.parent != None):
            if (parent.parent.left == parent):
                parent.parent.left = node #point to swtiching child node
                node.parent = parent.parent
                print(str(parent.parent.value) + " points left to "+str(node.value))
            elif (parent.parent.right == parent):
                parent.parent.right = node
                node.parent = parent.parent
                print(str(parent.parent.value) + " points right to "+str(node.value))
    #switch parent with child after pointer has been resolved
        if (parent.left != None):
            if (parent.left.value == node.value):
                pointer = parent.right
                if (node.left != None):
                    parent.left = node.left
                else:
                    parent.left = None
                if (node.right != None):
                    parent.right = node.right
                else:
                    parent.right = None
                node.right = pointer
                node.left = parent
        if (parent.right != None):
            if (parent.right.value == node.value):
                pointer = parent.left
                if (node.right != None):
                    parent.right = node.right
                else:
                    parent.right = None
                if (node.left != None):
                    parent.left = node.left
                else:
                    parent.left = None
                node.left = pointer
                node.right = parent

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

if __name__ == "__main__":
    print("running main")
    minHeap = MinHeap()
    minHeap.insert(8)
    minHeap.insert(20)
    minHeap.insert(40)
    minHeap.insert(25)
    minHeap.insert(30)
    minHeap.insert(50)
    minHeap.insert(44)
    minHeap.insert(80)
    print(minHeap.printInOrder())
    minHeap.insert(5)
    print(minHeap.printInOrder())
