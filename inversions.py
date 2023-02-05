def merge(arr, left, mid, right):
    i = left
    j = mid
    k = 0
    Count = 0
    itr=right-left+1
    temp = [0 for x in range(itr)]
 
    while i < mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
 
        else:
            temp[k] = arr[j]
            Count += mid - i
            k += 1
            j += 1
 
    while i < mid:
        temp[k] = arr[i]
        k += 1
        i += 1
 
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    
    k = 0
    for i in range(left, right + 1):
        arr[i] = temp[k]
        k += 1
    return Count
 
 
def mergeSort(arr, left, right):
    Count = 0
 
    if right > left:
        mid = (right + left) // 2
 
        Count = mergeSort(arr, left, mid)
        Count += mergeSort(arr, mid + 1, right)
        Count += merge(arr, left, mid + 1, right)
 
    return Count
 
 
if __name__ == '__main__':
    # k=int(input())
    # Arr = list(map(int, input().rstrip().split()))
    # k=2
    Arr=[2,4,1,3]
    print(mergeSort(Arr, 0, len(Arr)-1))

    # print(3//2)
    # print(Arr)
