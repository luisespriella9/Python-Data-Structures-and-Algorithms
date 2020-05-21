class QueueNode:
    value = None
    prev = None

class Queue:
    front = None
    back = None
    
    def _init_(self):
        #these are going to be dummy nodes
        self.front = None
        self.back = None
    
    def add(self, value):
        temporaryNode = QueueNode()
        temporaryNode.value = value
        if (self.front == None and self.back == None):
            self.front = temporaryNode
            self.back = temporaryNode
            '''
                prev for both of these will point to none
                so front and back will point to the same unti another one is added and will take the place of the back
                '''
        else:
            self.back.prev  = temporaryNode
            self.back = temporaryNode

    def remove(self):
        if (self.front != None):
            if (self.front == self.back):
                tempNode = self.front
                self.front = None
                self.back = None
            else:
                tempNode = self.front
                self.front = self.front.prev
            return tempNode
        return None

    def printQueue(self):
        iterator = self.front
        l = list()
        while (iterator!=None):
            l.append(iterator.value.value)
            iterator = iterator.prev
        return l

    def isEmpty(self):
        if (self.front == None and self.front == None):
            return True
        else:
            return False



if __name__ == "__main__":
    print("running main")
    queue = Queue()
    queue.remove()
    queue.add("otherside")
    queue.add("too far gone")
    print(queue.printQueue())
    queue.remove()
    queue.add("stairway to heaven")
    print(queue.printQueue())
    queue.remove()
    queue.remove()
    queue.remove()
    print(queue.printQueue())
