n = int(input())
ans = 0
i = 1
while n>0:
    ans += i * 9 * 10**(i-1)
    n-=9*10**(i-1)
    i+=1
ans += n*(i-1)
print(ans)
