from bisect import bisect
def find(A,x,k):
    res=[]
    if not A or k == 0:
       return res
    left_index=bisect(A,x)
    print(left_index)
    right_index=left_index
    left_index-=1
    for i in range(0,k):
        if left_index>0 and right_index<=len(A)-1:
            diff1=abs(float(A[left_index])-x)
            diff2=abs(float(A[right_index])-x)
            if diff1 > diff2:
                right_index+=1
                

#                 res.append(A[left_index])
#                 # A[left_index]=10000
            else:
                left_index-=1
#                 res.append(A[right_index])
#                 left_index+=1
#                 A[right_index]=-10
        else:
            if left_index<1:
                right_index+=1
            else:
                left_index-=1
    res=[A[i] for i in range(left_index+1,right_index)]
    return res






if __name__ == '__main__':
    # A=[4,1,3,2,7,4]
    # A=[1,2,3,4,4,7]
    A=[1,2,3,4,4,5,6]
    # x=6.5
    x=4
    # x=5.2
    k=5
    # k=2
    # find(A,x,k)
    print(A[1:6])
    res=find(A,x,k)
    print(res)