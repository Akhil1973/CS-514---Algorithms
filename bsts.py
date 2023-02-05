def bsts(n):
    if n==0:
        return n+1
    elif n==1:
        return n     
    
    arr = [0]*(n+1)
    # print(catalan)
    arr[0] = 1
    arr[1] = 1
    for i in range(2, n + 1):
        for j in range(i):
            arr[i] += arr[j] * arr[i-1-j]
    return arr.pop(-1)
 
 
if __name__ == '__main__':
    i=3
    print(bsts(i))