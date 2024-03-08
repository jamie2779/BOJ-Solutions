i=int(input())
p = sorted(map(int,input().split()))
res = 0
print(p)
for j in p:
    res += i*j
    i-=1
print(res)