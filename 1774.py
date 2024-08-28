import sys
input = sys.stdin.readline
n,m = map(int,input().split())
e = n*(n-1)//2
vertex = list(range(n))
rank = [0] * n
edge = []
tree = []

pos = [None] * n
for i in range(n):
    a,b = map(float,input().split())
    pos[i] = (a,b)

for i in range(m):
    a,b = map(int,input().split())
    edge.append((a-1,b-1,0))

for i in range(n):
    for j in range(i+1,n):
        d = ((pos[i][0] - pos[j][0])**2 +(pos[i][1] - pos[j][1])**2)**0.5
        edge.append((i,j,d))

def find_root(x):
    if vertex[x] != x:
        vertex[x] = find_root(vertex[x])  # 경로 압축
    return vertex[x]

def union(x, y):
    root_x = find_root(x)
    root_y = find_root(y)
    
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            vertex[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            vertex[root_x] = root_y
        else:
            vertex[root_y] = root_x
            rank[root_x] += 1


edge.sort(key=lambda x: x[2])
cycle = 0
for a,b,c in edge:
    if len(tree) == n-1:
        break
    if find_root(a) != find_root(b):
        union(a,b)
        tree.append(c)

print(f'{sum(tree):.2f}')