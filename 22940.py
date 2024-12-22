from fractions import Fraction

n = int(input())

nums = []
for i in range(n):
    row = map(int,input().split())
    nums.append([Fraction(i) for i in row])
    

for i in range(n):
    mul = i
    for j in range(i+1,n):
        if abs(nums[j][i]) > abs(nums[mul][i]):
            mul = j
    if mul != i:
        nums[i],nums[mul] = nums[mul],nums[i]
    
    mul = nums[i][i]
    if mul == 0:
        continue
    
    for j in range(n+1):
        nums[i][j] /= mul
    
    for j in range(n):
        if i != j:
            mul = nums[j][i]
            for k in range(n+1):
                nums[j][k] -= mul * nums[i][k]

for i in nums:
    print(int(i[-1]),end=" ")
            
