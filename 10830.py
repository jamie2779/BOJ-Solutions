n, b = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
memo = {1:a}

def mul(a,b):
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += a[i][k] * b[k][j]
            c[i][j] = s%1000
    return c

def pow(t):
    if t == 1:
        return a
    if t//2 not in memo:
        memo[t//2] = pow(t//2)
    if t % 2 == 0:
        return mul(memo[t//2],memo[t//2])
    else:

        return mul(mul(memo[t//2],memo[t//2]),a)
    

ans = pow(b)
for i in ans:
    for j in i:
        print(j%1000,end=" ")
    print()
