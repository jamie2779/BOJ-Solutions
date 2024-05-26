n, k = map(int,input().split())
items = [(0,0)]
for i in range(n):
    w,v = map(int,input().split())
    items.append((w,v))

memo = [[0] * (n+1) for _ in range(k+1)]
for i in range(k+1):
    for j in range(1,n+1):
        if i-items[j][0] >= 0:
            memo[i][j] = max(memo[i-items[j][0]][j-1]+items[j][1],memo[i][j-1])
        else:
            memo[i][j] = memo[i][j-1]
print(memo[-1][-1])
