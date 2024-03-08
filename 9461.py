n = int(input())
memo = {}
memo[1] = 1
memo[2] = 1
memo[3] = 1
memo[4] = 2
memo[5] = 2

def a(i):
    if i not in memo:
        memo[i] = a(i-1) + a(i-5)
    return memo[i]

for i in range(n):
    print(a(int(input())))