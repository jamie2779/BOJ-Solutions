n, m = map(int,input().split())
board = [[0 for i in range(m)] for j in range(n)]
visited = [[True for i in range(m)] for j in range(n)]
s = []
result = True
for i in range(n*3):
    s.append(input())

for i in range(n):
    for j in range(m):
        tile = []
        tile.append(s[3*i][3*j:3*j+3])
        tile.append(s[3*i+1][3*j:3*j+3])
        tile.append(s[3*i+2][3*j:3*j+3])

        if tile[1][1] in "01234":
            board[i][j] = int(tile[1][1])
        elif tile[1][1] == '.':
            visited[i][j] = False
            board[i][j] = 5
        elif tile[0][1] == '.' and tile[0][2] == '.':
            board[i][j] = 7
        elif tile[1][0] == '.' and tile[2][0] == '.':
            board[i][j] = 8
        elif tile[2][1] == '.' and tile[2][2] == '.':
            board[i][j] = 9
        elif tile[0][0] == '.' and tile[0][1] == '.':
            board[i][j] = 10
        else:
            board[i][j] = 6

def square1(r,c):
    if board[r][c] == 7:
        if r-1<0 or c+1>=m:
            return False
        if board[r-1][c] not in (5,9):
            return False
        if board[r][c+1] not in (5,10):
            return False
    elif board[r][c] == 8:
        if c-1<0 or r+1>=n:
            return False
        if board[r+1][c] not in (5,10):
            return False
        if board[r][c-1] not in (5,9):
            return False
    elif board[r][c] == 9:
        if r+1>=n or c+1>=m:
            return False
        if board[r+1][c] not in (5,7):
            return False
        if board[r][c+1] not in (5,8):
            return False
    elif board[r][c] == 10:
        if r-1<0 or c-1<0:
            return False
        if board[r-1][c] not in (5,8):
            return False
        if board[r][c-1] not in (5,7):
            return False
    elif board[r][c] == 5:
        if r-1 >=0:
            if board[r-1][c] == 8:
                if c+1 >= m or board[r][c+1] != 8:
                    return False
            elif board[r-1][c] == 9:
                if c-1 <0 or board[r][c-1] != 9:
                    return False
        if r+1 <n:
            if board[r+1][c] == 7:
                if c-1 < 0 or board[r][c-1] != 7:
                    return False
            elif board[r+1][c] == 10:
                if c+1 >= m or board[r][c+1] != 10:
                    return False
        
        #세로
        cnt = 0
        i = 0
        while True:
            if r-i<0:
                break
            if board[r-i][c] == 5:
                i+=1
                continue
            if board[r-i][c] in (8,9):
                for j in range(r-i+1,r):
                    visited[j][c] = True
                cnt+=1
            break
        i = 0
        while True:
            if r+i>=n:
                break
            if board[r+i][c] == 5:
                i+=1
                continue
            if board[r+i][c] in (7,10):
                for j in range(r,r+i+1):
                    visited[j][c] = True
                cnt+=1
            break
            
        if cnt == 1:
            return False
        #가로
        cnt = 0
        i = 0
        while True:
            if c-i<0:
                break
            if board[r][c-i] == 5:
                i+=1
                continue
            if board[r][c-i] in (7,9):
                for j in range(c-i+1,c):
                    visited[r][j] = True
                cnt+=1
            break
        i = 0
        while True:
            if c+i>=m:
                break
            if board[r][c+i] == 5:
                i+=1
                continue
            if board[r][c+i] in (8,10):
                for j in range(c,c+i):
                    visited[r][j] = True
                cnt+=1
            break
            
        if cnt == 1:
            return False
    
    return True

def triangle(r,c):
    cnt = 0
    if r-1 >=0 and board[r-1][c] in (7,8,9,10):
        cnt += 1
    if r+1 <n and board[r+1][c] in (7,8,9,10):
        cnt += 1
    if c-1 >=0 and board[r][c-1] in (7,8,9,10):
        cnt += 1
    if c+1 < m and board[r][c+1] in (7,8,9,10):
        cnt += 1
    if cnt == board[r][c]:
        return True
    else:
        return False
    
def square2(r,c):
    w = 0
    h = 1
    while c+w < m and not visited[r][c+w]:
        visited[r][c+w] = True
        w += 1
    while r+h < n and not visited[r+h][c]:
        for i in range(c,c+w):
            if visited[r+h][i]:
                return False
            visited[r+h][i] = True
        h+=1
    if r+h<n:
        for i in range(c,c+w):
            if not visited[r+h][i]:
                return False
        
    return True


for i in range(n):
    if not result:
        break
    for j in range(m):
        if board[i][j] <5:
            if not triangle(i,j):
                result = False
                break
        else:
            if not square1(i,j):
                result = False
                break

for i in range(n):
    if not result:
        break
    for j in range(m):
        if visited[i][j]:
            continue
        if not square2(i,j):
            result = False
            break




if result:
    print("YES")
else:
    print("NO")
