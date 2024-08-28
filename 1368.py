import sys
input = sys.stdin.readline
n = int(input())
vertex = list(range(n+1))
rank = [0] * (n+1)
edge = []
tree = []

for i in range(n):
    edge.append((0,i+1,int(input())))

mat = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(i+1,n):
        edge.append((i+1,j+1,mat[i][j]))

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
    if len(tree) == n:
        break
    if find_root(a) != find_root(b):
        union(a,b)
        tree.append(c)

print(sum(tree))