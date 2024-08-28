import sys
input = sys.stdin.readline
n = int(input())
b = [int(input()) for _ in range(n)]
a = [0] * 1000001
cnt = [0] * 1000001

for i in b:
    a[i] +=1

for i in range(1,1000000):
    cnt[i] += a[i] -1
    if a[i] > 0:
        for j in range(i * 2,1000001,i):
            cnt[j] += a[i]

for i in b:
    print(cnt[i])