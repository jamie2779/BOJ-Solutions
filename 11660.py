import sys
input = sys.stdin.readline
n,m=map(int,input().split())
memo = [[0]*(n+1) for _ in range(n+1)]

p = []
for i in range(n):
    p.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,n+1):
        memo[i][j] = memo[i-1][j] + memo[i][j-1] - memo[i-1][j-1] + p[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(memo[x2][y2] - memo[x1-1][y2] - memo[x2][y1-1]+memo[x1-1][y1-1])