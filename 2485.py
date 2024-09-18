import sys
input = sys.stdin.readline
def gcd(a, b):
    while b>0:
        a,b = b,a%b
    return a

t = []
n = int(input())
last = int(input())
mn = last
mx = last
for i in range(n-1):
    k = int(input())
    t.append(k-last)
    mn = min(mn,k)
    mx = max(mx,k)
    last = k

m = gcd(t[0],t[1])
for i in t[2:]:
    m = gcd(m,i)

print((mx - mn) // m - len(t))