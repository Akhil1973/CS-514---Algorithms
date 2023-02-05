import heapq as hq

def ksmallest(k,a):
    if a==[]:
        return a
    res = []
    for i in a:
        # print(i)
        if len(res) < k:
            
            hq.heappush(res, -i)
        else:
            if -i > res[0]:
                hq.heappop(res)
                # print(res)
                hq.heappush(res, -i)
    res = [-x for x in res]
    res.sort()
    return res




        


    


if __name__ == '__main__':
    
    print(ksmallest(2,[4, 1, 3, 5]))
    print(ksmallest(3, range(1000000, 0, -1)))