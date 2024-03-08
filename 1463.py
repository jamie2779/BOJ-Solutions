n = int(input())
memo = [0]*(n+1)
for i in range(2,n+1):
    k=[memo[i-1]]
    if i%3==0:
        k.append(memo[i//3])
    if i%2==0:
        k.append(memo[i//2])
    memo[i] = min(k)+1
print(memo[n])