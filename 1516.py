#1005번 코드 응용
n = int(input())

time = []
nlist = []
check = list(range(n))

for i in range(n):
    a = list(map(int,input().split()))
    time.append(a[0])
    nlist.append(a[1:-1])
dp = time.copy()

while len(check)>0:
    for i in check:
        if len(nlist[i]) == 0:
            for j in check:
                if i+1 in nlist[j]:
                    dp[j] = max(dp[j],dp[i]+time[j])
                    nlist[j].remove(i+1)
            check.remove(i)

print('\n'.join(map(str,dp)))