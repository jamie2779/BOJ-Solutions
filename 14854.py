#ref
#https://www.teferi.net/ps/%EC%9D%B4%ED%95%AD_%EA%B3%84%EC%88%98#%EB%AA%A8%EB%93%88%EB%9F%AC%EC%8A%A4%EA%B0%80_%EC%9E%84%EC%9D%98%EC%9D%98_%ED%95%A9%EC%84%B1%EC%88%98%EC%9D%BC_%EB%95%8C
#https://velog.io/@stripe2933/bj14854a

import sys
input = sys.stdin.readline

# 모듈러 역원
def inv_mod(a, m):
    if 1>=a:
        return 1
    else:
        return m - inv_mod(m%a,a) * m // a
    
def fact(p):
    fact = [1] * p
    for i in range(2, p):
        fact[i] = (fact[i-1] * i) % p
    return fact

def binomial_p(n, k, p, fact):
    if k > n or k < 0:
        return 0
    res = 1
    while k > 0 or n > 0:
        ni = n % p
        ki = k % p
        if ni < ki:
            return 0
        up = fact[ni]
        down = (fact[ki] * fact[ni - ki]) % p
        down = inv_mod(down, p) 
        res = (res * up * down) % p
        n //= p
        k //= p
    return res

#3의 배수 다 뺀거
def fact_3_27():
    fact = [1] * 27
    for i in range(2, 27):
        if i%3 == 0:
            fact[i] = fact[i-1]
        else:
            fact[i] = (fact[i-1] * i) % 27

    return fact

def binomial_27(n,m,fact):
    r = n-m
    n_j = []
    m_j = []
    r_j = []
    N_j = []
    M_j = []
    R_j = []
    e_j = []
    d=0
    tn,tm,tr = n,m,r
    while tn>0 or tm>0 or tr>0 or d<2:
        n_j.append(tn%3)
        m_j.append(tm%3)
        r_j.append(tr%3)
        tn//=3
        tm//=3
        tr//=3
        d+=1

    p = 1
    for i in range(d):
        N_j.append(n//p % 27)
        M_j.append(m//p % 27)
        R_j.append(r//p % 27)
        p*=3

    prev = 0
    for i in range(d):
        if m_j[i] + r_j[i] + prev >= 3:
            prev = 1
        else:
            prev = 0
        e_j.append(prev)
    e0 = sum(e_j)
    e2 = sum(e_j[2:])

    res = 1
    
    for i in range(d):
        res *= (fact[N_j[i]] * inv_mod(fact[M_j[i]],27) * inv_mod(fact[R_j[i]],27)) %27
    
    if e2 %2 == 1:
        res *= -1
    res *= 3**e0

    return res%27

fact11 = fact(11)
fact13 = fact(13)
fact27 = fact_3_27()
fact37 = fact(37)

N = 142857
p = [11, 13, 27, 37]
N_p = [N // i for i in p]
inv_p = [inv_mod(N_p[0], 11), inv_mod(N_p[1], 13), inv_mod(N_p[2], 27), inv_mod(N_p[3], 37)]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    # 각 모듈러에 대한 이항 계수 계산
    bi11 = binomial_p(n, m, 11, fact11)
    bi13 = binomial_p(n, m, 13, fact13)
    bi27 = binomial_27(n,m, fact27)
    bi37 = binomial_p(n, m, 37, fact37)


    # 중국인의 나머지 정리로 최종 결과 계산
    ans = (bi11 * N_p[0] * inv_p[0])+(bi13 * N_p[1] * inv_p[1])+(bi27 * N_p[2] * inv_p[2])+(bi37 * N_p[3] * inv_p[3])
    print(ans%N)
