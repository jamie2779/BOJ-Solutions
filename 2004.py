n, m = map(int,input().split())

cnt2 = 0
cnt5 = 0

def count(n,t):
    cnt = 0
    p=t
    while p<=n:
        cnt += n//p
        p*=t
    return cnt

cnt2 += count(n,2) - count(m,2) - count(n-m,2)
cnt5 += count(n,5) - count(m,5) - count(n-m,5)

print(min(cnt2,cnt5))