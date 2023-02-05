def find(A,x,k):
    
    A1=[]
    res=[]
    r=[]
    for i in A:
        A1.append(abs(x-i))    
    for j in range(k):        
        closest=min(A1)
        index=A1.index(closest)        
        res.append(index) 
        A1[index] =1000

    res.sort()
    for i in res:
        r.append(A[i])
    return r


if __name__ == '__main__':
    # A=[4,1,3,2,7,4]
    A=[5,3,4,1,6,3]
    # x=6.5
    x=3.5
    # k=3
    k=2
    res=find(A,x,k)
    print(res)