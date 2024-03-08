n,k = map(int,input().split())
r = 1
for i in range(n,n-k,-1):
    r*=i
for i in range(1,k+1):
    r //= i
print(r)