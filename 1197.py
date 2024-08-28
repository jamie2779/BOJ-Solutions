v,e = map(int,input().split())
vertex = [-1] * v
edge = [None]*e
tree = []
for i in range(e):
    a,b,c = map(int,input().split())
    edge[i] = (a-1, b-1, c)

def find_root(x):
    while True:
        if vertex[x] == x:
            return x
        x = vertex[x]
         


edge.sort(key=lambda x: x[2])
cycle = 0
for a,b,c in edge:
    if len(tree) == v-1:
        break
    if vertex[a] == -1 and vertex[b] == -1:
        vertex[a] = a
        vertex[b] = a
        tree.append(c)
    elif vertex[a] ==-1 and vertex[b] != -1:
        vertex[a] = b
        tree.append(c)
    elif vertex[a] != -1 and vertex[b] == -1:
        vertex[b] = a
        tree.append(c)
    else:
        root_a = find_root(a)
        root_b = find_root(b)
        if root_a != root_b:
            vertex[root_a] = vertex[root_b]
            tree.append(c)

print(sum(tree))