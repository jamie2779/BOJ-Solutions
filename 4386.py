import sys
input = sys.stdin.readline
v = int(input())
e = v*(v-1)//2
vertex = list(range(v))
rank = [0] * v
edge = []
tree = []

pos = [None] * v
for i in range(v):
    a,b = map(float,input().split())
    pos[i] = (a,b)

for i in range(v):
    for j in range(i+1,v):
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
    if len(tree) == v-1:
        break
    if find_root(a) != find_root(b):
        union(a,b)
        tree.append(c)

print(sum(tree))