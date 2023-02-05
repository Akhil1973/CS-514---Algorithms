def find(A):
    res=[]
    for i in range(len(A)):
        for j in range(i,len(A)):
            if A[i]+A[j] in A and A[i]!=A[j]:
                res.append((A[i],A[j],A[i]+A[j]))
    return res

    
if __name__ == '__main__':
    A=[1,4,2,3,5]
    res=find(A)
    print(res)