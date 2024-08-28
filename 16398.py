import sys
input = sys.stdin.readline
v =int(input())
vertex = list(range(v))
rank = [0] * v
edge = []
tree = []
mat = []
for i in range(v):
    mat.append(list(map(int,input().split())))
    
for i in range(v):
    for j in range(i+1,v):
        edge.append((i,j,mat[i][j]))

def find_root(x):
    if vertex[x] != x:
        vertex[x] = find_root(vertex[x])
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