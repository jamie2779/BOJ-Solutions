n,m,k = map(int,input().split())

b = [input() for i in range(n)];

c1 = []
c2 = []

for i in range(n):
    line = []
    line2 = []
    for j in range(m):
        if (i+j) %2 == 0:
            if b[i][j] == 'B':
                line.append(0)
                line2.append(1)
            else:
                line.append(1)
                line2.append(0)
        else:
            if b[i][j] == 'W':
                line.append(0)
                line2.append(1)

            else:
                line.append(1)
                line2.append(0)

    c1.append(line)
    c2.append(line2)

for i in range(n):
    for j in range(m):
        if i != 0:
            c1[i][j] += c1[i-1][j]
            c2[i][j] += c2[i-1][j]
        if j != 0:
            c1[i][j] += c1[i][j-1]
            c2[i][j] += c2[i][j-1]
        if i!= 0 and j!= 0:
            c1[i][j] -= c1[i-1][j-1]
            c2[i][j] -= c2[i-1][j-1]

def ch(c,i,j,k):
    res = 0
    res += c[i+k-1][j+k-1]
    if i != 0:
        res -= c[i-1][j+k-1]
    if j != 0:
        res -= c[i+k-1][j-1]
    if i != 0 and j != 0:
        res += c[i-1][j-1]
    return res

ans = k*k
for i in range(n-k+1):
    for j in range(m-k+1):
        ans = min(ans,ch(c1,i,j,k))
        ans = min(ans,ch(c2,i,j,k))

print(ans)