n = int(input())

res = n
primes = [2,3,5,7,11,13,17,19,23,29]

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
                return True
            for _ in range(s-1):
                x = pow(x,2,n)
                if x == n-1:
                    return True
    return False
    

def g(x):
    return (x*x+1)%n

def gcd(a,b):
    while b > 0:
        c = a%b
        a = b
        b = c
    return a
nums = set()
def div(n):
    while not isPrime(n):
        x = 2
        y = 2
        d = 1

        while d == 1:
            x = g(x)
            y = g(g(y))
            d = gcd(abs(x-y), n)

        if d == n:
            break
        else:
            if isPrime(d):
                if d not in nums:
                    res *= (1-1/d)
                    nums.add(d)
                n //= d
            else:
                div(d)

    if n >1:
        if n not in nums:
                res *= (1-1/n)


print(int(res))