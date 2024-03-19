n = int(input())
p = list(map(int,input().split()))

ans = 0

for i in range(n):
    if i+2 <n and i+1<n:
        if p[i+1]>p[i+2]:
            tmp = min(p[i+1] - p[i+2],p[i])
            ans += tmp*5
            p[i] -= tmp
            p[i+1] -= tmp
    if i+2<n:
        tmp = min(p[i],p[i+1],p[i+2])
        ans += tmp*2
        p[i+2] -=tmp
    if i+1<n:
        tmp = min(p[i],p[i+1])
        ans += tmp*23
        p[i+1] -=tmp
    ans += p[i]*3
    p[i] = 0
print(ans)