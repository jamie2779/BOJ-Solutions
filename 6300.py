import sys
input = sys.stdin.readline
#l,c,w 입력받기
l, c, w = map(int,input().split())
#보드 입력받기
board = []
for i in range(l):
    board.append(input().strip())
#단어 입력받기
words = []
for i in range(w):
    words.append(input().strip())

#방향 미리 설정
directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

#단어, x, y, 방향을 입력받아 보드에서 비교(d는 튜플형태의 방향)
def compWord(target,x,y, d):
    for letter in target:
        if x<0 or x>=c or y<0 or y>=l:
            return False
        if board[y][x] != letter:
            return False
        x += d[0]
        y -= d[1]
    return True

#보드 왼쪽 위부터 오른쪽 아래로 8방향을 둘러보며 단어 찾기
for word in words:
    flag = False
    for i in range(l):
        for j in range(c):
            for k in range(8):
                if compWord(word,j,i,directions[k]):
                    print(i,j,chr(k+65))
                    flag = True
                    break
            if flag:
                break
        if flag:
            break

