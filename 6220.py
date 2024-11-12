import sys
sys.setrecursionlimit(10**6)
c, n = map(int,input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
ans = 0
memo = {0:0}

def dp(a):
    if a<0:
        return 1001
    if a not in memo:
        memo[a] = min([dp(a-i) for i in coins]) + 1           
    return memo[a]

print(dp(c))