n, m = map(int,input().split())

gh = list(map(int,input().split()))
mh = list(map(int,input().split()))
tg = list(map(int,input().split()))
tm = list(map(int,input().split()))

edge = [[]for i in range(n)]

for i in range(n):
    for j in range(m):
        if gh[i] > tm[j] and mh[j] < tg[i]:
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

