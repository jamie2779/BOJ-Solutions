from collections import deque
import sys
input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    c = input().split()
    if c[0] == "push":
        q.append(c[1])
    elif c[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif c[0] == "size":
        print(len(q))
    elif c[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif c[0] == "front":
        if q:
            print(q[0])
        else:   
            print(-1)
    else:
        if q:
            print(q[-1])
        else:   
            print(-1)
        
        