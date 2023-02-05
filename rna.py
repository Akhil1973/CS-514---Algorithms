from collections import defaultdict
from heapq import heapify,heappush,heappop

def _match(a, b):
    if (a == 'A' and b == 'U') or (b == 'A' and a == 'U'):
        return True
    elif (a == 'G' and b == 'C') or (b == 'G' and a == 'C'):
        return True
    elif (a == 'G' and b == 'U') or (b == 'G' and a == 'U'):
        return True
    else:
        return False

def _print(l, back):
    tmp = ['.']*l
    result = ''
    for i in back:
        tmp[i[0]] = '('
        tmp[i[1]-1] = ')'
    for j in tmp:
        result += j
    return result

def best(rna):
    cache = defaultdict(int)
    back = defaultdict(lambda:[])
    
    def _best(i, j):
        if (i, j) in cache or i==j:
            return cache[i, j]
        if i+1 == j:
            return cache[i, j-1]
        tmp = -1
        if _match(rna[i],rna[j-1]):
            tmp = _best(i+1, j-1) + 1
            back[i, j] = back[i+1, j-1] + [(i,j)]
        for k in range(i+1, j):
            if tmp < _best(i, k) + _best(k, j):
                tmp = _best(i, k) + _best(k, j)
                back[i, j] = back[i, k] + back[k, j]
        cache[i, j] = tmp
        return cache[i, j]
    i, j = 0, len(rna)
    res = _best(i, j)
    return res, _print(j, back[i, j])

def total(s):
    opt, l = defaultdict(int), len(s)
    for i in range(l+1):
        opt[i,i], opt[i,i+1] = 1, 1 

    for d in range(2,l+1):  
        for i in range(0,l-d+1):
            j = i+d 
            opt[i,j] += opt[i+1,j]      
            for k in range(i+2,j+1):    
                if s[i]+s[k-1] in {'AU','UA','CG','GC','UG','GU'}:
                    opt[i,j]+= opt[i+1,k-1] * opt[k,j]
    return opt[0,l]
 

def kbest(s, k):  
    opt = defaultdict(lambda:[(0,-2,0,0)])
    def solution(i, j, a):
        if i >= j: 
            return ""
        mid = opt[i,j][a][1]
        if mid == i+1:     
            return "." + solution(mid, j, opt[i,j][a][3])
        elif mid > i+1:      
            return "("+solution(i+1,mid-1,opt[i,j][a][2])+")" + solution(mid,j,opt[i,j][a][3])
        else:
            return "."*(j-i)     
    l, res = len(s), []
    if s == '': 
        return [(0, "")]
    for d in range(2,l+1):  
        for i in range(l-d+1):
            j = i+d            
            h = [(0,-2,0,0)]
            if opt[i+1,j][0][0] < 0:
                h.append((opt[i+1,j][0][0], i+1, 0, 0))  
            for mid in range(i+2,j+1):  
                if s[i]+s[mid-1] in {'AU','UA','CG','GC','UG','GU'}:  
                    h.append((opt[i+1,mid-1][0][0]+opt[mid,j][0][0]-1, mid, 0, 0))
                else:
                    continue
            heapify(h)  
            if h[0][0] == 0:   
                continue    
            opt[i,j] = []
            used = set()
            for _ in range(k):
                opt[i,j].append(heappop(h))
                n, mid, a, b = opt[i,j][-1]
                if mid == -2: 
                    break     
                elif mid == i+1:          
                    if b < len(opt[mid,j])-1 and opt[mid,j][b+1][0] < 0:  
                        heappush(h,(opt[mid,j][b+1][0], mid, 0, b+1))
                else:                   
                    a1, b1 = a+1, b+1
                    if a1 < len(opt[i+1,mid-1]) and not (mid, a1, b) in used:
                        heappush(h,(opt[i+1,mid-1][a1][0]+opt[mid,j][b][0]-1, mid, a1, b))
                        used.add((mid,a1,b))
                    if b1 < len(opt[mid,j]) and not (mid, a, b1) in used:
                        heappush(h,(opt[i+1,mid-1][a][0]+opt[mid,j][b1][0]-1, mid, a, b1))
                        used.add((mid,a,b1))
    for a, (n,_,_,_) in enumerate(opt[0,l]):
        res.append((-n,solution(0,l,a)))
    return res 

print(best("GCACG"))
print(total('ACAGU'))
print(total('UUUGGCACUA'))
print(total('GAUGCCGUGUAGUCCAAAGACUUC'))
print(total('AGGCAUCAAACCCUGCAUGGGAGCG'))
print(kbest('CCCGGG',10))
print(kbest('CCCGGG',10))