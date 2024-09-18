n, k = map(int,input().split())
value = []
for i in range(n):
    value.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for v in value:
    for j in range(v,k+1):
        dp[j] += dp[j-v]
    
print(dp)
