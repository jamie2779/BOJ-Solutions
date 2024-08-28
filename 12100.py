import sys
sys.setrecursionlimit(10**6)
n = int(input())
#0 = 왼쪽, 1=오른쪽, 2=위쪽, 3=아래쪽
mx = 0

def move(board,dir):
    global mx
    b = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if dir == 0:
                b[i][j] = board[i][j]
            elif dir == 1:
                b[i][j] = board[i][n-j-1]
            elif dir == 2:
                b[i][j] = board[j][n-i-1]
            elif dir == 3:
                b[i][j] = board[n-j-1][i]

    new = []
    for i in range(n):
        col = []
        target = -1
        for j in range(n):
            if b[i][j] !=0:
                if target != -1:
                    if b[i][target] == b[i][j]:
                        col.append(b[i][target]*2)
                        target = -1
                    else:
                        col.append(b[i][target])
                        target = j
                else:
                    target = j 
            if col and col[-1]>mx:
                mx = col[-1]
        if target != -1:
            col.append(b[i][target])
        while len(col) < n:
            col.append(0)
        new.append(col)

    for i in range(n):
        for j in range(n):
            if dir == 0:
                b[i][j] = new[i][j]
            elif dir == 1:
                b[i][j] = new[i][n-j-1]
            elif dir == 2:
                b[i][j] = new[n-j-1][i]
            elif dir == 3:
                b[i][j] = new[j][n-i-1]
    return b

board = []
for i in range(n):
    board.append(list(map(int,input().split())))

mx = board[0][0]
for i in range(4):
    b1 = move(board,i)
    for j in range(4):
        b2 = move(b1,j)
        for k in range(4):
            b3 = move(b2,k)
            for l in range(4):
                b4 = move(b3,l)
                for m in range(4):
                    b5 = move(b4,m)

print(mx)