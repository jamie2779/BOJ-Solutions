def solve(n,m,a):
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

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

while True:
    n,m = map(int,input().split())
    if(n==0 and m == 0):
        break
    blue = []
    red = []
    for i in range(n//10 if n%10 == 0 else n//10+1):
        blue += list(map(int,input().split()))
    for i in range(m//10 if m%10 == 0 else m//10+1):
        red += list(map(int,input().split()))
    a = [[]for i in range(n)]
    for i in range(n):
        for j in range(m):
            if gcd(blue[i], red[j]) > 1:
                a[i].append(j)
    print(solve(n,m,a))