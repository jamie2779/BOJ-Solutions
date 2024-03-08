#with pypy3
input()
a = list(map(int,input().split()))
x = int(input())
cnt = 0
for i in a:
    if x-i in a:
        cnt+=1
print(cnt//2)
