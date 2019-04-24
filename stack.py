'''
implementation of a stack
'''
class StackNode():
    value = None
    nextNode = None

class Stack():
    top = None
    
    def __init__(self):
        self.top = None
    
    def push(self, value):
        temporaryNode = StackNode()
        temporaryNode.value = value
        
        if (self.top == None):
            self.top = temporaryNode
        else:
            temporaryNode.nextNode = self.top
            self.top = temporaryNode

def pop(self):
    if (self.top != None):
        if (self.top.nextNode != None):
            self.top = self.top.nextNode
        else:
            self.top = None

def printStack(self):
    iterator = stack.top
    l = list()
    while (iterator != None):
        l.append(iterator.value)
        iterator = iterator.nextNode
    return l

def peak(self):
    return self.top.value

if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    print(stack.peak())
    print(stack.printStack())
    stack.pop()
    print(stack.printStack())
    stack.pop()
    print(stack.printStack())
