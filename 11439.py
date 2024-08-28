n, k, m = map(int,input().split())

#에라토스테네스의 체
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
p = [x for x in range(2, n + 1) if is_prime[x]]

#펙토리얼 한 값 소인수분해 구하기
def fact_prime(n):
    res = {}
    for i in p:
        pp = i
        while pp<=n:
            res[i] = res.get(i,0)+n//pp
            pp*=i
    return res

#분할정복 거듭제곱
def div_pow(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

n_p = fact_prime(n)
k_p = fact_prime(k)
nk_p = fact_prime(n-k)
bi_p = {}
for k in n_p:
    i = n_p[k] - (k_p.get(k,0)+nk_p.get(k,0))
    if i>0:
        bi_p[k] = i

res = 1
for k in bi_p:
    res = (res * div_pow(k, bi_p[k], m)) % m

print(res)