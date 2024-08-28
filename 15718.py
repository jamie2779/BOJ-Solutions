import sys
input = sys.stdin.readline
p = 97
fact97 = [-1] * (p)
fact97[0] = 1
fact97[1] = 1
for i in range(2,p):
    fact97[i] = (fact97[i-1] * i) %p

p = 1031
fact1031 = [-1] * (p)
fact1031[0] = 1
fact1031[1] = 1
for i in range(2,p):
    fact1031[i] = (fact1031[i-1] * i) %p


def binomial97(n,k):
    if k>n or k<0:
        return 0
    p=97
    res = 1
    while k >0 or n >0:
        ni = n%p
        ki = k%p
        
        if ni<ki:
            res = 0
            break
        up = fact97[ni]
        down = (fact97[ki]*fact97[ni-ki])%p
        down = pow(down,p-2,p)
        res = (res * up * down) % p        
        n //= p
        k //= p
    return res

def binomial1031(n,k):
    if k>n or k<0:
        return 0
    p=1031
    res = 1
    while k >0 or n >0:
        ni = n%p
        ki = k%p
        
        if ni<ki:
            res = 0
            break
        up = fact1031[ni]
        down = (fact1031[ki]*fact1031[ni-ki])%p
        down = pow(down,p-2,p)
        res = (res * up * down) % p        
        n //= p
        k //= p
    return res

inv97 = pow(97,1029,1031)
inv1031 = pow(1031,95,97)

t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    if m-1 == n:
        print(1)
        continue
    #m-1개 중 n-m+1 개를 뽑는 중복조합
    # (m-1)+(n-m+1)-1 C m-2
    
    m1 = binomial97(n-1, m-2)
    m2 = binomial1031(n-1, m-2)
    ans = ((m1 * 1031 * inv1031 ) + (m2 * 97 * inv97))%100007
    print(ans)