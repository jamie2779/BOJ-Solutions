import random
import sys
sys.setrecursionlimit(10**6)
n = int(input())

res = n
primes = [2,3,5,7,11,13,17,19,23,29,31,37]

def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    s = 0
    d = n-1
    while d%2 == 0:
        d //=2
        s += 1
    
    for a in primes:
        if a < n:
            x = pow(a,d,n)
            if x == 1 or x == n-1:
                continue
            for _ in range(s-1):
                x = pow(x,2,n)
                if x == n-1:
                    break
            else:
                return False
    return True
    
def g(x,c):
    return (x*x+c)%n

def gcd(a,b):
    while b > 0:
        c = a%b
        a = b
        b = c
    return a

def div(n):
    if isPrime(n):
        return n
    if n %2 == 0:
        return 2
    
    init = random.randint(2,n)
    c = random.randint(1,n)
    x = init
    y = init
    d = 1

    while d == 1:
        x = g(x,c)
        y = g(g(y,c),c)
        d = gcd(abs(x-y), n)

    if d == n:
        return div(n)
    if isPrime(d):
        return d
    else:
        return div(d)

nums = {}
while n>1:
    d = div(n)
    if d not in nums:
        nums[d] = 0
    nums[d]+=1
    n//=d

res = 1
for i in nums:
    res *= nums[i]+1

print(res)