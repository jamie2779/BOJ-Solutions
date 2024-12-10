n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split()))[1:])
selected = [-1] * (m+1)

def sol(n):
    if visited[n]:
        return False
    visited[n] = True

    for i in a[n]:
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

