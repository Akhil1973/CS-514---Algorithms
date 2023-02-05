from collections import defaultdict, namedtuple
from heapq import heappush, heappop

tuples = namedtuple('tuples', 'opt back matched')
mapping = {'A': set(['U']), 'G': set(['C','U']), 'U': set(['A','G']), 'C': set(['G'])}



def best(seq):
    dp = defaultdict(lambda: tuples(float('-inf'), -1, False))

    for i in range(len(seq)):
        dp[i, i] = tuples(0, -1, False)
        dp[i, i-1] = tuples(0, -1, False)

    for k in range(1, len(seq)):
        for i in range(len(seq)-k):
            j = i + k
            for t in range(i, j):
                if (seq[j] in mapping[seq[t]]) or (seq[t] in mapping[seq[j]]):
                    dp[i, j] = max(dp[i, j], tuples(1 + dp[i, t-1].opt + dp[t+1, j-1].opt, t, True))

            dp[i, j] = max(dp[i,j], tuples(dp[i, j-1].opt, dp[i, j-1].back, False))
    opt, opt_t, _ = dp[0, len(seq)-1]
    return opt, _backtrack(seq, dp, 0, opt_t, len(seq)-1)

def _backtrack(seq, dp, i, t, j):
    res = ['.' for _ in seq]
    _backtrack_helper(res, dp, i, t, j)
    return ''.join(res)

def _backtrack_helper(res, dp, i, t, j):
    if t == -1:
        return
    if dp[i, j].matched:
        res[t], res[j] = '(', ')'
        _backtrack_helper(res, dp, i, dp[i, t-1].back, t-1)
        _backtrack_helper(res, dp, t+1, dp[t+1, j-1].back, j-1)
    else:
        _backtrack_helper(res, dp, i, dp[i, j-1].back, j-1)


def total(seq):
    dp = defaultdict(int)
    for i in range(len(seq)):
        dp[i, i] = 1
        dp[i, i-1] = 1

    for k in range(1, len(seq)):
        for i in range(len(seq)-k):
            j = i + k
            for t in range(i, j):
                if (seq[j] in mapping[seq[t]]) or (seq[t] in mapping[seq[j]]):
                    dp[i, j] += dp[i, t-1] * dp[t+1, j-1]
            dp[i, j] += dp[i, j-1]

    return dp[0, len(seq)-1]

sets = set(['AU','UA','CG','GC','GU','UG'])
def kbest(s, k):

    def kbest_helper(s_arr, start, end):
        if start < len(opt[i, s_arr-1]) and end < len(opt[s_arr+1, j-1]) \
           and not (s_arr, start, end) in used:
            used.add((s_arr, start, end))
            heappush(heap, 
                     (-(opt[i, s_arr-1][start][0]+opt[s_arr+1, j-1][end][0] + 1), s_arr, start, end))

    def kbest_helper1(index):
        if index < len(opt[i, j-1]):
            heappush(heap, (-opt[i, j-1][index][0], index))

    n = len(s)
    opt = defaultdict(list) 
    for i in range(n):
        opt[i, i] = [(0, '.')] 
        opt[i, i-1] = [(0, '')]

    for span in range(2, n+1): 
        for i in range(n-span+1): 
            j = i+span-1 

            heap = []            
            used = set()

            for m in range(i, j): 
                if s[m]+s[j] in sets: 
                    kbest_helper(m, 0, 0)
            kbest_helper1(0) 

            uniq = set()
            for _ in range(k):
                if heap == []: 
                    break
                item = heappop(heap)
                if len(item) == 2: 
                    value, index = item
                    opt[i, j].append((-value, "%s." % opt[i,j-1][index][1]))
                    kbest_helper1(index+1)
                else: 
                    value, s_arr, start, end = item
                    opt[i, j].append((-value, "%s(%s)" % (opt[i, s_arr-1][start][1],
                                                          opt[s_arr+1, j-1][end][1])))
                    kbest_helper(s_arr, start+1, end)
                    kbest_helper(s_arr, start, end+1)

    return opt[0,n-1]

print(best('GUUAGAGUCU'))
print(total('ACAGU'))
print(kbest('ACAGU',3))
print(kbest("ACAGU", 3))