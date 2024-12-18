n, m = map(int,input().split())

tee = []
for _ in range(n):
    tee.append(int(input()))
kara = []
for _ in range(m):
    kara.append(int(input()))

edge = [[]for i in range(n)]

for i in range(n):
    for j in range(m):
        w = tee[i]
        k = kara[j]
        if (w/2<=k and k<= w*3/4) or (w<=k and k<=w*5/4):
            edge[i].append(j)
    
selected = [-1] * (m+1)

def sol(n):
    if visited[n]:
        return False
    visited[n] = True

    for i in edge[n]:
        if selected[i] == -1 or sol(selected[i]):
            selected[i] = n
            return True
    return False

for i in range(n):
    visited = [False] * n
    sol(i)

s = 0
for i in selected:
    if i != -1:
        s += 1
print(s)

