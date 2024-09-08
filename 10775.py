import sys
input = sys.stdin.readline

# Union-Find
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# Union-Find
def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    parent[rootX] = rootY

g = int(input())  
p = int(input())  

parent = list(range(g + 1)) 

cnt = 0
for _ in range(p):
    gi = int(input())
    docking_gate = find(parent, gi)

    if docking_gate == 0:
        break

    union(parent, docking_gate, docking_gate - 1)
    cnt += 1

print(cnt)
