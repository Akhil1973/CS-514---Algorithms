from collections import defaultdict

def longest(v, e):
    def topo(v, e):
        q = []
        d = []
        s = []
        for n in range(v):
            d.append(0)
            s.append([])
        for t in e:
            s[t[0]].append(t[1])
            d[t[1]] += 1
        for n in range(v):
            if d[n] == 0:
                q.append(n)
        for n in q:
            for sn in s[n]:
                d[sn] -= 1
                if d[sn] == 0:
                    q.append(sn)
        return q, s

    tvl, svl = topo(v, e)
    if tvl == []: return (0, [])
    dl = defaultdict(int)
    dlp = {}
    for tv in tvl:
        for sv in svl[tv]:
            if dl[tv] + 1 > dl[sv]:
                dl[sv] = dl[tv] + 1
                dlp[sv] = tv
    n = tvl[-1]
    l = dl[n]
    lp = [n]
    while n in dlp:
        n = dlp[n]
        lp = [n] + lp
    return (l, lp)


if __name__ == '__main__':
    print(longest(8, [(0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (5, 6), (5, 7)]))
    