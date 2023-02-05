def checkbitStrings(arr):
    res= [c1 == c2 and c2==0 for c1, c2 in zip(arr, arr[1:])]
    print(res)
 

def generateAllBinaryStrings(n, arr, i):
 
    if i == n:
        checkbitStrings(arr)
        # print(arr)
        

    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)
 
# Driver Code
if __name__ == "__main__":
 
    n = 3
    arr = [None] * n
    arr=generateAllBinaryStrings(n, arr, 0)
    print(arr)
 