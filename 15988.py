a = [int(input()) for i in range(int(input()))]
target = max(a)
save = [1] * (target + 1)
save[1] = 1
save[2] = 2
save[3] = 4
for i in range(4,target+1):
    save[i] = (save[i-1] + save[i-2] + save[i-3])%1000000009

for i in a:
    print(save[i]%1000000009)