import sys
sys.setrecursionlimit(10**8)
memo = {}
memo[0] = 0
memo[1] = 1
memo[2] = 1

def dp(i):
    if i not in memo:
        if i%2==0:
            memo[i] = (dp(i//2) * (dp(i//2) + 2*dp(i//2-1)))%1_000_000_007
        else:
            memo[i] = (dp(i//2)**2 + dp(i//2+1)**2)%1_000_000_007
    return memo[i]

n = int(input())
print(dp(n))