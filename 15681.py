#DFS | 트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n,r,q = map(int,input().split())
child = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    child[a].append(b)
    child[b].append(a)

visited = [False]*(n+1)
cnt = [1] * (n+1)

def dfs(node):
    visited[node] = True
    for i in child[node]:
        if not visited[i]:
            cnt[node] += dfs(i)
    return cnt[node]

dfs(r)

for i in range(q):
    target = int(input())
    print(cnt[target])