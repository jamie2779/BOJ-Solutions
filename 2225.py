p = 1000000000
n, k = map(int,input().split())

memo = [[0 for _ in range(n+1)] for _ in range(k+1)]

for i in range(1, k+1):
    for j in range(n+1):
        if i == 1:
            memo[i][j] = 1
        else:
            for l in range(j+1):
                memo[i][j] += memo[i-1][l]
print(memo[-1][-1]%p)




