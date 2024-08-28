n, k, m = map(int,input().split())
fact = [-1] * (m)
fact[0] = 1
fact[1] = 1
for i in range(2,m):
    fact[i] = (fact[i-1] * i) %m

res = 1

while k >0 or n >0:
    ni = n%m
    ki = k%m
    
    if ni<ki or ki<0:
        res = 0
        break
    up = fact[ni]
    down = (fact[ki]*fact[ni-ki])%m
    down = pow(down,m-2,m)
    res *= (up * down) % m
    res %= m
    
    n //= m
    k //= m

print(res%m)