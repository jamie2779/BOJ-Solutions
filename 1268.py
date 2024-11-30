n = int(input())

c = []
res = [0]*n

for i in range(n):
    c.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(5):
                if c[i][k] == c[j][k]:
                    res[i] += 1
                    break

m = max(res)
print(res.index(m)+1)