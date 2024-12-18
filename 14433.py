def matching(n,m, a):
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
    return s

n,m,k1,k2 = map(int,input().split())
a = [[]for _ in range(n)]
for _ in range(k1):
    i,j = map(int,input().split())
    a[i-1].append(j-1)
res1 = matching(n,m,a)

a = [[]for _ in range(n)]
for _ in range(k2):
    i,j = map(int,input().split())
    a[i-1].append(j-1)
res2 = matching(n,m,a)

if res1>res2:
    print("그만 알아보자")
else:
    print("네 다음 힐딱이")
