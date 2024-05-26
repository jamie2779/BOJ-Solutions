a = input()
b = input()
memo = [[0]*(len(b)+1) for _ in range((len(a)+1))]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])

print(memo[-1][-1])
