import sys
input = sys.stdin.readline
v = int(input())
vertex = list(range(v))
rank = [0] * v
edge = []
tree = []

planet = []
for i in range(v):
    a,b,c = map(int,input().split())
    planet.append((i,a,b,c))

def culc(a,b):
    _,x1,y1,z1 = planet[a]
    _,x2,y2,z2 = planet[b]
    return min(abs(x1-x2),abs(y1-y2),abs(z1-z2))

for key in range(1,4):
    planet.sort(key = lambda x:x[key])
    for i in range(1,v):
        i1,_,_,_ = planet[i-1]
        i2,_,_,_ = planet[i]
        edge.append((i1,i2,culc(i-1,i)))

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