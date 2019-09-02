class ListNode():
    value = None
    next = None
class LinkedList():
    head = None
    
    def _init_(self):
        self.head = None
    
    def insertAt(self, x, value):
        tempNode = ListNode()
        tempNode.value = value
        if (x == 0): #inserting at head
            tempNode.next = self.head
            self.head = tempNode
            return
        i = 0
        iterator = self.head
        while (i != x-1 and iterator.next != None):
            i += 1
            iterator = iterator.next
        if (i == x-1):
            if (iterator.next != None):
                tempNode.next = iterator.next
            else:
                tempNode.next = None
            iterator.next = tempNode

    def appendToTail(self, value):
        tempNode = ListNode()
        tempNode.value = value
        if (self.head == None):
            self.head = tempNode
        else:
            iterator = self.head
            while (iterator.next != None):
                iterator = iterator.next
            iterator.next = tempNode

    def delete(self, value):
        iterator = self.head
        if (self.head.value == value):
            if (self.head.next != None):
                self.head = self.head.next
            else:
                self.head = None
            return
        while (iterator.next != None):
            if (iterator.next.value == value):
                if (iterator.next.next != None):
                    iterator.next = iterator.next.next
                else:
                    iterator.next = None
                break
            iterator = iterator.next

    def printList(self):
        result = ""
        iterator = self.head
        while (iterator != None):
            result += str(iterator.value) + "->"
            iterator = iterator.next
        result += "None"
        return result

    def size(self):
        if (self.head == None):
            return 0
        iterator = self.head
        i = 0
        while (iterator != None):
            i += 1
            iterator = iterator.next
        return i


if __name__ == "__main__":
    print("running main")
    linkedList = LinkedList()
    linkedList.appendToTail(5)
    linkedList.appendToTail(8)
    linkedList.insertAt(1, 6)
    print(linkedList.printList())
    print(linkedList.size())
    linkedList.delete(8)
    linkedList.delete(5)
    print(linkedList.printList())
