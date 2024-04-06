a, b = map(int,input().split())
c = sorted(list(map(int,input().split())))

def p(n1,n2, m):
    if m == 1:
        return [(c[i],) for i in range(n1,n2)]
    else:
        res = []
        for i in range(n1, n2):
            for j in p(i,n2,m-1):
                res.append((c[i],)+j)
        return res

res = list(set(p(0,a,b)))
for i in range(1,b+1):
    res.sort(key=lambda x: x[-i])

for i in res:
    print(*i)