from linkedList import *

class HashTable():
    arr = [None]*10
    for i in range(len(arr)):
        l = LinkedList()
        arr[i] = l

    def hashf(self, value):
        return value % 10

    def insert(self, value):
        key = self.hashf(value)
        l = self.arr[key]
        l.insertAtTail(value)
    
    def printHashTable(self):
        for x in self.arr:
            print(x.printList())




if __name__ == "__main__":
    print("running main")
    hashTable = HashTable()
    hashTable.insert(11)
    hashTable.insert(23)
    hashTable.insert(36)
    hashTable.insert(9)
    hashTable.insert(11)
    hashTable.insert(2)
    hashTable.insert(26)
    hashTable.insert(5)
    hashTable.insert(44)
    hashTable.insert(97)
    hashTable.printHashTable()
