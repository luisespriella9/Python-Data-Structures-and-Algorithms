'''
run with python2
binary search, returns index
iterative way of binary searching
better than recursively -> takes less space?
recursive always takes at least O(N) space
'''

def search(array, value):
    left = 0
    right = len(array)-1
    while (left<=right):
        mid = int((left+right)/2)
        if (array[mid]==value):
            return mid
        if (value < array[mid]):
            right = mid-1
        elif (value > array[mid]):
            left = mid+1
    return None

arr = [4,7,9,12,15,18,20]

#returns range(0, 7) and then None because 1 is not in list
print(search(arr, 4))
print(search(arr, 7))
print(search(arr, 9))
print(search(arr, 12))
print(search(arr, 15))
print(search(arr, 18))
print(search(arr, 20))
print(search(arr, 1)) #returns none

