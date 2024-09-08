#pypy로 해야 통과
board = [list(map(int,input())) for _ in range(9)]
rec = [[0 for _ in range(3)] for _ in range(3)]
row = [0] * 9
col = [0] * 9


for i in range(9):
    for j in range(9):
        n = board[i][j]
        if n != 0:
            rec[i//3][j//3] += 1<<n
            row[i] += 1<<n
            col[j] += 1<<n


def is_valid(rec,row,col, r, c, num):
    if rec[r//3][c//3] & (1<<num):
        return False
    if row[r] & (1<<num):
        return False
    if col[c] & (1<<num):
        return False
    return True

def solve(board):
    for r in range(9):  
        for c in range(9):
            if board[r][c] == 0:
                for num in range(1, 10):
                    if is_valid(rec,row,col, r, c, num):
                        rec[r//3][c//3] += 1<<num
                        row[r] += 1<<num
                        col[c] += 1<<num
                        board[r][c] = num
                        if solve(board):
                            return True
                        board[r][c] = 0
                        rec[r//3][c//3] -= 1<<num
                        row[r] -= 1<<num
                        col[c] -= 1<<num
                return False
    return True


solve(board)

for row in board:
    print("".join(map(str, row)))