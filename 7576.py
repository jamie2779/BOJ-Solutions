x,y = map(int,input().split())
target = set()
queue = []
next = []
ans = 0
for i in range(y):
    a = input().split()
    for j in range(x):
        if a[j] == '1':
            next.append((i,j))
        elif a[j] == '0':
            target.add((i,j))


while target and next:
    while next:
        queue.append(next.pop())
    while queue:
        i,j = queue.pop()
        for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            if (i+di,j+dj) in target:
                target.remove((i+di,j+dj))
                next.append((i+di,j+dj))
    ans+=1
if target:
    print(-1)
else:
    print(ans)





