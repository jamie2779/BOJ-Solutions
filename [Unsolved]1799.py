n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]


black = [[0 for _ in range(n)] for _ in range(n)]
white = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i+j) %2 == 0:
            black[i][j] = board[i][j]
        else:
            white[i][j] = board[i][j]

def put(board,i,j):
    new = []
    for col in board:
        new.append(col[:])
    for d in range(n):
        for dx, dy in ((-1,-1),(-1,1),(1,-1),(1,1)):
            dxi = dx*d + i
            dyi = dy*d + j
            if 0<=dxi and dxi<n and 0<=dyi and dyi<n:
                new[dxi][dyi] = 0``
    new[i][j] = 2
    return new


mx_b = 0
a = [black]
while a:
    now = a.pop()
    cnt = sum([i.count(2) for i in now])
    if cnt>mx_b:
        mb = now
    mx_b = max(mx_b,cnt)
    if cnt + sum([i.count(1) for i in now]) < mx_b:
        continue
    for i in range(n):
        for j in range(n):
            if now[i][j] == 1:
                a.append(put(now,i,j))

mx_w = 0
a = [white]
while a:
    now = a.pop()
    cnt = sum([i.count(2) for i in now])
    mx_w = max(mx_w,cnt)
    if cnt + sum([i.count(1) for i in now]) < mx_w:
        continue
    for i in range(n):
        for j in range(n):
            if now[i][j] == 1:
                a.append(put(now,i,j))  

print(mx_b+mx_w)