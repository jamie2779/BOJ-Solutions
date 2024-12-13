n,m = map(int,input().split())
exp = [[]for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    exp[a-1].append(b-1)

selected = [-1] * (n+1)

def sol(n):
    if visited[n]:
        return False
    visited[n] = True

    for i in exp[n]:
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

