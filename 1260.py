from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**6)


n,m,v = map(int,input().split())
nodes = defaultdict(lambda :[])
for _ in range(int(m)):
    a,b = map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)


#DFS
visited = [False]*(n+1)
stack = deque([v])
def dfs(i):
    print(i, end=" ")
    visited[i] = True
    nodes[i].sort(reverse=True)
    for j in nodes[i]:
        stack.append(j)
    
    while True:
        if len(stack)==0:
            return
        tmp = stack.pop()
        if not visited[tmp]:
            break
    dfs(tmp)

#BFS
visited2 = [False]*(n+1)
queue = deque([v])
def bfs(i):
    print(i, end=" ")
    visited2[i] = True
    nodes[i].sort()
    for j in nodes[i]:
        queue.append(j)
    
    while True:
        if len(queue)==0:
            return
        tmp = queue.popleft()
        if not visited2[tmp]:
            break
    bfs(tmp)

    
dfs(v)
print()
bfs(v)

