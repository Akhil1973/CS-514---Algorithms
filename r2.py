def memoize(f):
    d = dict()

    def wrapper(*args):
        if args in d:
            return d[args]
        else:
            result = f(*args)
            d[args] = result
            return result

    return wrapper

pairs = frozenset(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])

sets=set(['AU', 'UA', 'CG', 'GC', 'GU', 'UG'])
def best(s):
    @memoize
    def b(i, j):
        if j - i < 2:
            return 0, False, None
        else:
            m = 0, False, None
            if s[i] + s[j-1] in pairs:
                m = b(i+1, j-1)[0] + 1, True, None
            for k in range(i+1, j):
                if b(i, k)[0] + b(k, j)[0] > m[0]:
                    m = b(i, k)[0] + b(k, j)[0], False, k
            return m
    b_RES = ['.'] * len(s)

    def backtrace(i, j):
        _, x, k = b(i, j)
        if x:
            b_RES[i] = '('
            b_RES[j-1] = ')'
            backtrace(i+1, j-1)
        elif k is not None:
            backtrace(i, k)
            backtrace(k, j)

    backtrace(0, len(s))

    return b(0, len(s))[0], ''.join(b_RES)

def total(s):
    @memoize
    def t(i, j):
        if j - i < 2:
            return 1
        else:
            tot = 0
            for k in range(i+1, j):
                if s[i] + s[k] in pairs:
                    tot += t(i+1, k) * t(k+1, j)
            return tot + t(i+1, j)

    return t(0, len(s))


from heapq import heappop, heappush
from collections import defaultdict

def kbest(rna, k):
    def _kbest(i,j):

        
        def try_heappush1(p):
            if p < len(def_dict[i+1,j-1]):
                heappush(h, (-(def_dict[i+1,j-1][p][0]+1),(p,)))


        def try_heappush(s,p,q):
            if p < len(def_dict[i,s]) and q < len(def_dict[s+1,j]) and (s,p,q) not in visited:
                heappush(h,(- (def_dict[i,s][p][0] + def_dict[s+1,j][q][0]),(s,p,q)))
                visited.add((s,p,q))


        if (i,j) in def_dict:
            return def_dict[i,j]

        elif i==j:
            def_dict[i,j] = [(0,'.')]
            return None
        elif j == i-1:
            def_dict[i,i-1] = [(0,'')]
            return None

        h = []
        visited = set()
        for s in range(i,j):
            _kbest(i,s)
            _kbest(s+1,j)
            try_heappush(s, 0,0)

        if rna[i]+rna[j] in sets:
            _kbest(i+1,j-1)
            try_heappush1(0)

        find = 0
        while find < k:
            if h == []:
                # print("debug")
                break
            score, indices = heappop(h)
            
            try:
                s,p,q = indices
                ans = (-score, "%s%s" % (def_dict[i,s][p][1],def_dict[s+1,j][q][1]))

                if ans not in def_dict[i, j]:
                    def_dict[i, j].append(ans)
                    find += 1
                    

                try_heappush(s,p+1,q)
                try_heappush(s,p,q+1)
            except:
                p = indices[0]
                ans = (-score, "(%s)" % def_dict[i+1,j-1][p][1])
                # print(ans) debug

                if ans not in def_dict[i,j]:
                    def_dict[i, j].append(ans)
                    find += 1

                try_heappush1(p+1)

    def_dict = defaultdict(list)
    _kbest(0,len(rna)-1)
  
    return _kbest(0,len(rna)-1)

print(best('GUUAGAGUCU'))
print(total('ACAGU'))
print(kbest('CCCGGG',10))