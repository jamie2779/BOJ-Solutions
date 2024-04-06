a, b = map(int,input().split())
c = sorted(list(map(int,input().split())))

def p(n1,n2, m):
    if m == 1:
        return [[c[i]] for i in range(n1,n2)]
    else:
        res = []
        for i in range(n1, n2):
            for j in p(i,n2,m-1):
                res.append([c[i]]+j)
        return res
    
for i in p(0,a,b):
    print(*i)