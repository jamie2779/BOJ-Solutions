a, b = map(int,input().split())

def p(n1,n2, m):
    if m == 1:
        return [[i] for i in range(n1,n2+1)]
    else:
        res = []
        for i in range(n1, n2+1):
            for j in p(i,n2,m-1):
                res.append([i]+j)
        return res
    
for i in p(1,a,b):
    print(*i)