import random

mod = 1000000007

def ipow(x, p):
    ret, piv = 1, x
    while p > 0:
        if p & 1:
            ret = (ret * piv) % mod
        piv = (piv * piv) % mod
        p >>= 1
    return ret

def berlekamp_massey(x):
    ls, cur = [], []
    lf, ld = 0, 0
    for i in range(len(x)):
        t = 0
        for j in range(len(cur)):
            t = (t + x[i-j-1] * cur[j]) % mod
        if (t - x[i]) % mod == 0:
            continue
        if len(cur) == 0:
            cur = [0]*(i+1)
            lf = i
            ld = (t - x[i]) % mod
            continue
        k = -((x[i] - t) * ipow(ld, mod - 2) % mod)
        c = [0]*(i - lf - 1)
        c.append(k)
        for val in ls:
            c.append((-val * k) % mod)
        if len(c) < len(cur):
            c += [0]*(len(cur) - len(c))
        for j in range(len(cur)):
            c[j] = (c[j] + cur[j]) % mod
        if i - lf + len(ls) >= len(cur):
            ls, lf, ld = cur, i, (t - x[i]) % mod
        cur = c
    for i in range(len(cur)):
        cur[i] = (cur[i] % mod + mod) % mod
    return cur

def get_nth(rec, dp, n):
    m = len(rec)
    s = [0]*m
    t_ = [0]*m
    s[0] = 1
    if m != 1:
        t_[1] = 1
    else:
        t_[0] = rec[0]
    def mul(v, w):
        t = [0]*(2*m)
        for j in range(m):
            for k in range(m):
                t[j+k] = (t[j+k] + v[j]*w[k]) % mod
        for j in range(2*m-1, m-1, -1):
            for k in range(1, m+1):
                t[j-k] = (t[j-k] + t[j]*rec[k-1]) % mod
        return t[:m]
    while n > 0:
        if n & 1:
            s = mul(s, t_)
        t_ = mul(t_, t_)
        n >>= 1
    ret = 0
    for i in range(m):
        ret = (ret + s[i]*dp[i]) % mod
    return ret

def guess_nth_term(x, n):
    if n < len(x):
        return x[n]
    v = berlekamp_massey(x)
    if not v:
        return 0
    return get_nth(v, x, n)

def get_min_poly(n, M):
    rng = random.Random(0x14004)
    randint = lambda lb, ub: rng.randint(lb, ub)
    rnd1, rnd2 = [], []
    for _ in range(n):
        rnd1.append(randint(1, mod - 1))
        rnd2.append(randint(1, mod - 1))
    gobs = []
    for _ in range(2*n + 2):
        tmp = 0
        for j in range(n):
            tmp = (tmp + rnd2[j]*rnd1[j]) % mod
        gobs.append(tmp)
        nxt = [0]*n
        for e in M:
            nxt[e[0]] = (nxt[e[0]] + e[2]*rnd1[e[1]]) % mod
        rnd1 = nxt
    sol = berlekamp_massey(gobs)
    sol.reverse()
    return sol


n,k = map(int,input().split())

dp = [[0]*104 for _ in range(51)]
for i in range(104):
    dp[0][i] = i

for i in range(1, 51):
    for j in range(104):
        for l in range(1,j+1):
            dp[i][j] += dp[i-1][l]
            dp[i][j] %= mod

print(guess_nth_term(dp[n],k))