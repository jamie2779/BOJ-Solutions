p = 1000000007
n = int(input())
s = list(map(int,input().split()))

s.sort()
t = 0
for i in range(n):
    t += (s[-i-1]%p - s[i]%p) * pow(2,n-1-i,p)
print(t%p)