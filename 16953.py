from collections import deque
a, b = map(int,input().split())
ans = 1
target = deque([a])
next = deque()
while True:
    if len(target)==0:
        if len(next) == 0:
            print(-1)
            break
        ans += 1
        target = next
        next = deque()
    else:
        t = target.pop()
        if t == b:
            print(ans)
            break
        elif t < b:
            next.append(t*2)
            next.append(t*10+1)