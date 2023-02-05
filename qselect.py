from random import randint

def qselect(k,Arr):
    if len(Arr)==0:
        return -1
    ran= randint(0,len(Arr)-1)
    # pivot=Arr[ran]
    pivot=Arr.pop(ran)
    left_part= [x for x in Arr if x<=pivot]    
    right_part=[x for x in Arr if x>pivot]    
    if len(left_part)==k-1:
        return pivot
    elif len(left_part)>k-1:
        return qselect(k,left_part)
    else:
        return qselect(k-1-len(left_part),right_part)


if __name__ == '__main__':
    k=int(input())
    Arr = list(map(int, input().rstrip().split()))
    # k=2
    # Arr=[3,10,4,7,19]
    res=qselect(k,Arr)
    print(res)
