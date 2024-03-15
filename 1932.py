n=int(input())
p = []
memo = [[0]*n for _ in range(n)]

for i in range(n):
    p.append(list(map(int,input().split())))
memo[0][0] = p[0][0]

for i in range(1,n):
    for j in range(i+1):
        target = [memo[i-1][j]]
        if j != 0:
            target.append(memo[i-1][j-1])
        memo[i][j] = max(target) + p[i][j]

print(max(memo[-1]))