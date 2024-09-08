n = int(input())
last = 0
cnt = 0
ans = [0 for i in range(10)]

while n>0:
    now = n%10
    for i in range(10):
        ans[i] += now * cnt * 10**cnt // 10
    ans[now] += last + 1
    for i in range(now):
        ans[i] += 10**cnt
    last += now * 10**cnt
    ans[0] -= 10**cnt
    cnt +=1
    n //= 10

for i in ans:
    print(i, end=' ')