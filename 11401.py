n, k = map(int,input().split())
p = 1000000007

def factorial(a):
    res = 1
    for i in range(1,a+1):
        res = res * i %p
    return res

up = factorial(n)
down = (factorial(k)*factorial(n-k))%p
down = pow(down,p-2,p)

print(up * down %p)