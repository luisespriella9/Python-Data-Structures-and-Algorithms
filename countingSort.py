inp = [9, 4, 10, 8, 2, 4]

def counting_sort(arr, max_number):
    count = [0 for i in range(max_number+1)]
    for x in arr:
        count[x]+=1;
    for i in range(len(count)):
        if i != max_number+1 and i!=0:
            count[i] += count[i-1]
    sorted_list = [0 for i in range(len(arr)+1)]
    for x in arr:
        index = count[x]
        sorted_list[index] = x
        count[x]-=1
    return sorted_list[1::]


if __name__ == "__main__":
    print(counting_sort(inp, 10))
    p2 = [5,9,20,1,4,6,2,8,10]
    print(counting_sort(p2, 20))