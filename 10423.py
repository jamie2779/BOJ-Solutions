import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
vertex = list(range(n))
rank = [0] * n
edge = []
tree = []
source = list(map(int,input().split()))
for i in source[1:]:
    edge.append((source[0]-1,i-1,0))

for i in range(m):
    a,b,c = map(int,input().split())
    edge.append((a-1, b-1, c))

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
    if len(tree) == n-1:
        break
    if find_root(a) != find_root(b):
        union(a,b)
        tree.append(c)

print(sum(tree))