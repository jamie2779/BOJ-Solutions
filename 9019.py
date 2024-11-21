from collections import deque

n = int(input())

def bfs(a,b):
    visited = set()
    queue = deque()
    queue.append((a,""))
    while True:
        now, res = queue.popleft()
        if now == b:
            return res
        #D
        next = 2*now%10000
        if next not in visited:
            queue.append((next,res+"D"))
            visited.add(next)
        #S
        next = 9999 if now == 0 else now-1
        if next not in visited:
            queue.append((next,res+"S"))
            visited.add(next)
        #L
        next = ((now*10) + (now//1000))%10000
        if next not in visited:
            queue.append((next,res+"L"))
            visited.add(next)
        #R
        next = (now//10) + (now%10*1000)
        if next not in visited:
            queue.append((next,res+"R"))
            visited.add(next)
for i in range(n):
    a,b = map(int,input().split())
    print(bfs(a,b))
    
    