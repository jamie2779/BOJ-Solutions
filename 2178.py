n,m = map(int,input().split())
maze = []
for i in range(m):
    maze.append(input().split())
a = ['0 0','+']
cnt = 0
target = f'{n-1} {m-1}'
print(maze)
while target not in a:
    print(a)
    k = a.pop()
    if k == '+':
        cnt += 1
        a.append('+')
    else:
        x,y = map(int,k.split())
        if x>0 and maze[y][x-1] == "1": a.append(f'{x-1} {y}')
        if y>0 and maze[y-1][x] == "1": a.append(f'{x} {y-1}')
        if x<m and maze[y][x+1] == "1": a.append(f'{x+1} {y}')
        if y<n and maze[y+1][x] == "1": a.append(f'{x} {y+1}')
print(cnt)