n = int(input())
numbers = list(map(int,input().split()))
memo = [0]*n

for i in range(n):
    target = [0]
    for j in range(i):
        if numbers[j] < numbers[i]:
            target.append(memo[j])
    memo[i] = max(target)+1
print(max(memo))