from collections import deque

n, k = map(int, input().split())
queue = deque()
pos = {n}

queue.append((n, 0))

while True:
    now, cnt = queue.popleft()
    
    if now == k:
        print(cnt)
        break
    
    if now * 2 not in pos and now < k:
        queue.append((now * 2, cnt + 1))
        pos.add(now * 2)
    
    if now + 1 not in pos:
        queue.append((now + 1, cnt + 1))
        pos.add(now + 1)
    
    if now - 1 not in pos:
        queue.append((now - 1, cnt + 1))
        pos.add(now - 1)
