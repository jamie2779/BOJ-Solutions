x,y,z = map(int,input().split())
target = set()
queue = []
next = []
ans = 0
for i in range(z):
    for j in range(y):
        a = input().split()
        for k in range(x):
            if a[k] == '1':
                next.append((i,j,k))
            elif a[k] == '0':
                target.add((i,j,k))

while target and next:
    while next:
        queue.append(next.pop())
    while queue:
        i,j,k = queue.pop()
        for di,dj,dk in [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]:
            if (i+di,j+dj,k+dk) in target:
                target.remove((i+di,j+dj,k+dk))
                next.append((i+di,j+dj,k+dk))
    ans+=1
if target:
    print(-1)
else:
    print(ans)





