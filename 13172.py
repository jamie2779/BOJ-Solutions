##메모리 초과 때문에 각 단계에서 모듈러 해야함
##분할정복을 이용한 거듭제곱 써야함(구현 귀찮아서 pow 썼음)

import sys
sys.setrecursionlimit(10**6)
m = int(input())
p = 1000000007
down = 1
up = 0
for i in range(m):
    n, s = map(int,input().split())
    up *= n%p
    up %= p
    up += (down * s)%p
    up %= p
    down*=n%p

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

g = gcd(up,down)
up//=g
down//=g

print((up%p * pow(down,p-2,p))%p)
