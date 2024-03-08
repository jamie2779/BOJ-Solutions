n, p, q = map(int,input().split())
memo = {}
memo[0] = 1

def a(i):
    if i not in memo:
        memo[i] = a(i//p) + a(i//q)
    return memo[i]

print(a(n))



