from collections import deque

# 이동할 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 탐색
def bfs(red, blue):
    q = deque()
    q.append((red[0], red[1], blue[0], blue[1], 0))  # 빨간 구슬, 파란 구슬 좌표와 이동 횟수
    visited = set()
    visited.add((red[0], red[1], blue[0], blue[1]))
    
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        
        # 10번 이상 움직이면 실패
        if cnt >= 10:
            return -1
        
        # 네 방향으로 기울이기
        for i in range(4):
            nrx, nry, r_count = move(rx, ry, dx[i], dy[i])
            nbx, nby, b_count = move(bx, by, dx[i], dy[i])
            
            # 파란 구슬이 구멍에 빠지면 실패
            if board[nbx][nby] == 'O':
                continue
            
            # 빨간 구슬이 구멍에 빠지면 성공
            if board[nrx][nry] == 'O':
                return cnt + 1
            
            # 두 구슬이 같은 위치에 있을 때 처리
            if nrx == nbx and nry == nby:
                if r_count > b_count:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            # 이전에 방문한 적이 없으면 큐에 삽입
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, cnt + 1))
    
    # 10번 이내에 빨간 구슬을 구멍에 넣지 못하면 실패
    return -1

# 구슬을 굴리는 함수
def move(x, y, dx, dy):
    count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

# 입력 처리
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

red = blue = None

# 보드에서 빨간 구슬, 파란 구슬 위치 찾기
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'B':
            blue = (i, j)
            board[i][j] = '.'

# BFS 실행
result = bfs(red, blue)
print(result)
