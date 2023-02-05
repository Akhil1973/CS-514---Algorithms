from collections import defaultdict
from heapq import heappop,heappush
def shortest(n, edges):
    start, end = 0, n-1
    npop,npush = 0,0
    def solution(v, back):
        if v == start: return [v]
        return solution(back[v],back)+[v]

    edge = defaultdict(set)
    back = {}
    d    = defaultdict(lambda: 1<<30)
    for (u,v,w) in edges:
        edge[u].add((v,w))
        edge[v].add((u,w))  
    
    h = [(0,start,-1)]  # (dist,node,prev)
    while len(h):
        dist, u, prev = heappop(h)
        npop += 1
        if u in back: continue
        back[u] = prev
        if u == end: return dist, solution(end,back)
        for v, w in edge[u]:
            if v not in back:          # v not popped yet   
                if dist+w < d[v]:
                    heappush(h,(dist+w, v, u))
                    d[v] = dist+w
                    npush += 1
    return None


if __name__ == "__main__":

    print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
    # (4, [0,1,2,3])
    print(shortest(5,[(0,2,24),(0,4,20),(3,0,3),(4,3,12)]))
    #(15, [0, 3, 4])
    print(shortest(4, [(0,1,1), (2,3,1)]))
