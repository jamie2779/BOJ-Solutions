n,p = map(int,input().split())
res = 1
for i in range(1,n+1):
    res *= i
    res %= p
print(res)