import sys
input = sys.stdin.readline
while True:
    v,e = map(int,input().split())
    total = 0
    if v==0 and e==0:
        break
    vertex = list(range(v))
    rank = [0] * v
    edge = [None]*e
    tree = []
    for i in range(e):
        a,b,c = map(int,input().split())
        edge[i] = (a-1, b-1, c)
        total += c

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

    print(total - sum(tree))