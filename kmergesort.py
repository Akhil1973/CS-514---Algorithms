import heapq as hq
def kmergesort(arr, k):
    
    n = len(arr)
    if n == 1:
        return arr
    k = k if n > k else n
    step = n // k
    part_arr = []
    for i in range(0, n, step):
        temp = kmergesort(arr[i:i+step], k)
        part_arr.append(temp)
    return kmerge(part_arr)

def kmerge(arr):
    merged = []
    heap = []
    print(arr)
    for i, lst in enumerate(arr):
        hq.heappush(heap, (lst[0], i, 1))
    # print(merge_heap)
    while len(heap) != 0:
        val, idx, i_val = hq.heappop(heap)
        print(val,idx,i_val)
        merged.append(val)
        if i_val < len(arr[idx]):
            hq.heappush(heap, (arr[idx][i_val], idx, i_val+1))
    return merged

if __name__ == '__main__':
    
    print(kmergesort([4,1,5,3,2,6,9,7],3))
    i=4
    print(-i)