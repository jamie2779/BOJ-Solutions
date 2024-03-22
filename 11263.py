import sys

def rec(n,s):
    if n == 1 and s < 10:
        return 1
    elif s > n*9:
        return 0
    c = 0
    for i in range(10): 
        if s-i>=0:
            c += rec(n-1,s-i)
    return c

for c in sys.stdin:
    n, s = map(int,c.split())
    print(rec(n,s))
