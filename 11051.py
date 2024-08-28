import sys
sys.setrecursionlimit(10**6)
n, k = map(int,input().split())
p = 10007

def factorial(a,cnt):
    if cnt == 0:
        return a
    return factorial((a * cnt)%p,cnt-1)

up = factorial(1,n)
down = (factorial(1,k)*factorial(1,n-k))%p
down = down**(p-2)%p


print(up * down %p)