n = int(input())
p = list(map(int,input().split()))

ans = 0

for i in range(n-1,-1,-1):
    if i-2>=0:
        tmp = min(p[i],p[i-1],p[i-2])
        ans += tmp*2
        p[i-2] -=tmp
    if i-1>=0:
        tmp = min(p[i],p[i-1])
        ans += tmp*2
        p[i-1] -=tmp
    ans += p[i]*3
    p[i] = 0

print(ans)