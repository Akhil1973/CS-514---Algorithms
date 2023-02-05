def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        print(mid)
        left=arr[:mid]
        # print(left)
        right=arr[mid:]
        # print(right)
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        # j=0
        # k=0
        while  i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1




if __name__ == '__main__':
    # k=int(input())
    # Arr = list(map(int, input().rstrip().split()))
    # k=2
    Arr=[3,10,4,7,19,12,11]
    mergeSort(Arr)
    print(Arr)
