def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = int(input())

def t(num, n):
    if isPrime(num):
        if 10**(n-1)<=num and num < 10**n:
            print(num)
        else:
            for i in range(1,10):
                t(num*10+i,n)

for i in range(1,10):
    t(i,n)
        