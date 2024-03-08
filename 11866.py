from collections import deque
n,k = map(int,input().split())
lst = deque(range(1,n+1))

r = []
while lst:
    for i in range(k-1):
        lst.append(lst[0])
        lst.popleft()
    r.append(str(lst.popleft()))
print(f'<{", ".join(r)}>')