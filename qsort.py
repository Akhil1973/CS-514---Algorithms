def sort(Arr):
    if Arr==[]:
        return []
    else:
        pivot=Arr[0]
        left=[x for x in Arr if x<pivot]
        right=[x for x in Arr[1:] if x>=pivot]
        return [sort(left)]+[pivot]+[sort(right)]

def sorted(Arr):
    # Not using predefined sort function so added the same quick sort method again.
    if Arr==[]:
        return []
    else:
        pivot=Arr[0]
        left=[x for x in Arr if x < pivot]
        right=[x for x in Arr[1:] if x >= pivot]
        return sorted(left) + [pivot] + sorted(right)

def search(Arr,x):
    for i in Arr:
        if i==x:
            return True
    else:
        return False

def insert(Arr,x):
    if search(Arr,x):
        return sort(Arr)
    else:
        Arr.append(x)
        return sort(Arr)

if __name__ == '__main__':
    # k=int(input())
    # Arr = list(map(int, input().rstrip().split()))
    tree=[4,2,6,3,5,7,1,9]
    Arr1=sort(tree)
    print(Arr1)
    Arr1=insert(tree,6.5)
    print(Arr1)
    Arr1=insert(tree,6)
    print(Arr1)
    Arr1=sorted(tree)
    print(Arr1)    
    print(search(tree,6.5))
    print(search(tree,8.5))
    # print(Arr)
