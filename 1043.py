#그래프 안쓰고 set로 해결함
n, m = map(int,input().split())
t = set(input().split()[1:])
p = [set(input().split()[1:]) for _ in range(m)]
pt = [0] * m
count = 0
flag = True
while flag:
    flag = False
    for i in range(m):
        if len(t&p[i]) == 0:
            pt[i] = 1
        else:
            pt[i] = 0
            if len(p[i]-t) != 0:
                t |= p[i]
                flag = True

print(sum(pt))