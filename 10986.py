n,m = map(int,input().split())

s = [0]

for i in map(int,input().split()):
    s.append(i)
    s[-1] += s[-2]
    s[-1] %= m

cnt = 0

for i in range(m):
    c = s.count(i)
    cnt += c*(c-1)//2
print(cnt)

