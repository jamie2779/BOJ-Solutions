n, m = map(int, input().split())
a = ['0' * (m + 1)] + ['0' + input() for _ in range(n)]
b = [[0] * (m + 1) for _ in range(n + 1)]
mx = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i][j] == '1':
            b[i][j] = min(b[i - 1][j], b[i][j - 1], b[i - 1][j - 1]) + 1
            mx = max(mx, b[i][j])

print(mx ** 2)
