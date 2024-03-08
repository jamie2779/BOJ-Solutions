
n = int(input())
memo = [[-1]*(n+1) for i in range(n+1)]
matrix = [()]
for i in range(n):
    c,r = map(int,input().split())
    matrix.append((c,r))


def dp(i,j):
    if memo[i][j] == -1:
        if i == j:
            memo[i][j] = 0
        else:
            test = []
            for k in range(i,j):
                test.append(dp(i,k)+dp(k+1,j)+matrix[i][0] * matrix[k][1] * matrix[j][1])
            memo[i][j] = min(test)
    return memo[i][j]

print(dp(1,n))
