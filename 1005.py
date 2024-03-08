import sys
input = sys.stdin.readline
t = int(input())

for _t in range(t):
    n,k = map(int,input().split())
    time = list(map(int,input().split()))
    dp = time.copy()
    nlist = [[] for _ in range(n)]
    check = list(range(n))
    for i in range(k):
        x,y = map(int,input().split())
        nlist[y-1].append(x-1)
    while len(check)>0:
        for i in check:
            if len(nlist[i]) == 0:
                for j in check:
                    if i in nlist[j]:
                        dp[j] = max(dp[j],dp[i]+time[j])
                        nlist[j].remove(i)
                check.remove(i)
    
    w = int(input())
    print(dp[w-1])