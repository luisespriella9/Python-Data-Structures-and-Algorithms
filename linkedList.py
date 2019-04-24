class ListNode():
    value = None
    nextNode = None
class LinkedList():
    head = None
    
    def _init_(self):
        self.head = None
    
    def insertAt(self, x, value):
        tempNode = ListNode()
        tempNode.value = value
        if (x == 0): #inserting at head
            tempNode.nextNode = self.head
            self.head = tempNode
            return
        i = 0
        iterator = self.head
        while (i != x-1 and iterator.nextNode != None):
            i += 1
            iterator = iterator.nextNode
        if (i == x-1):
            if (iterator.nextNode != None):
                tempNode.nextNode = iterator.nextNode
            else:
                tempNode.nextNode = None
            iterator.nextNode = tempNode

    def insertAtTail(self, value):
        tempNode = ListNode()
        tempNode.value = value
        if (self.head == None):
            self.head = tempNode
        else:
            iterator = self.head
            while (iterator.nextNode != None):
                iterator = iterator.nextNode
            iterator.nextNode = tempNode

    def remove(self, value):
        iterator = self.head
        if (self.head.value == value):
            if (self.head.nextNode != None):
                self.head = self.head.nextNode
            else:
                self.head = None
            return
        while (iterator.nextNode != None):
            if (iterator.nextNode.value == value):
                if (iterator.nextNode.nextNode != None):
                    iterator.nextNode = iterator.nextNode.nextNode
                else:
                    iterator.nextNode = None
                break
            iterator = iterator.nextNode

    def printList(self):
        l = list()
        iterator = self.head
        while (iterator != None):
            l.append(iterator.value)
            iterator = iterator.nextNode
        return l

    def size(self):
        if (self.head == None):
            return 0
        iterator = self.head
        i = 0
        while (iterator != None):
            i += 1
            iterator = iterator.nextNode
        return i


if __name__ == "__main__":
    print("running main")
    linkedList = LinkedList()
    linkedList.insertAtTail(5)
    linkedList.insertAtTail(8)
    linkedList.insertAt(1, 6)
    print(linkedList.printList())
    print(linkedList.size())
    linkedList.remove(8)
    linkedList.remove(5)
    print(linkedList.printList())
