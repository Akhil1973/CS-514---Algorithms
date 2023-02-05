from collections import defaultdict

def order(v, e):
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
        return q

print(order(5, [(0,1), (1,2), (2,3), (3,4)]))
print(order(5, []))
print(order(3, [(1,2), (2,1)]))
#    [0, 1, 2, 3, 4] )
