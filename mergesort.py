arr = [8,5,3,7,1,4,9,2]
arr3 = [8,46,90,24,36,17,3,27,38,16,2,5]

def mergesort(arr):
    if (len(arr)==1):
        return arr
    return merge(mergesort(arr[0:int(len(arr)/2)]),mergesort(arr[int(len(arr)/2):]))

def merge(arr1, arr2):
    p1 = 0
    p2 = 0
    l = []
    while (p1 != len(arr1) and p2 != len(arr2)):
        if (arr1[p1] < arr2[p2]):
            l.append(arr1[p1])
            p1+=1
        else:
            l.append(arr2[p2])
            p2+=1
    while (p1 != len(arr1)):
        l.append(arr1[p1])
        p1+=1
    while (p2 != len(arr2)):
        l.append(arr2[p2])
        p2+=1
    return l

arr1 = [2,4,7,9]
arr2 = [3,5,8]
#print(merge(arr1, arr2)) #testing merge
print(mergesort(arr))
print(mergesort(arr3))
