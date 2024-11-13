n,m = map(int,input().split())

a = []
b = []
for i in range(n):
    a.append(list(map(int,input())))

for i in range(n):
    b.append(list(map(int,input())))

c = [[a[i][j] != b[i][j] for j in range(m)] for i in range(n)]

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if c[i][j]:
            cnt += 1
            for k in range(3):
                for l in range(3):
                    c[i+k][j+l] = not c[i+k][j+l]

if any([any(c[i]) for i in range(n)]):
    print("-1")
else:
    print(cnt)