#quicksort.py

arr = [8, 5, 3, 7, 1, 4, 9, 2]

def quicksort(arr, leftPointer = 0, rightPointer = len(arr)-1):
    leftStart = leftPointer
    rightStart = rightPointer
    
    if (len(arr[leftPointer:rightPointer])<=1):
        return
    median = arr[int((leftPointer+rightPointer)/2)]
    
    while (leftPointer <= rightPointer):
        if (arr[leftPointer]>=median and arr[rightPointer]<=median):
            swap(leftPointer, rightPointer)
            leftPointer+=1
            rightPointer-=1
        while (arr[leftPointer]<median):
            leftPointer+=1
        while (arr[rightPointer]>median):
            rightPointer-=1

    if (leftPointer <= rightPointer):
        quicksort(arr, leftStart, leftPointer)
        quicksort(arr, rightPointer, rightStart)
    else:
        quicksort(arr, leftStart, rightPointer+1)
        quicksort(arr, leftPointer, rightStart)



def swap(x, y):
    #print("swapping "+str(arr[x])+" and "+str(arr[y]))
    temp1 = arr[x]
    temp2 = arr[y]
    arr[x] = temp2
    arr[y] = temp1

quicksort(arr)
print(arr)
