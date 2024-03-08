import sys
input = sys.stdin.readline
#l,c,w 입력받기
l, c, w = map(int,input().split())
#보드 입력받기
board = []
for i in range(l):
    board.append(input().strip())
#단어 입력받기
answer = {}
words = []
for i in range(w):
    word = input().strip()
    words.append(word)

#트리 만들기
class node:
    def __init__(self, output=False):
        self.output = output
        self.child = {}

wordTree = node()

def addTree(_tree, _word):
    """
    :param node _tree:
    :param str _word:
    :return:
    """
    if len(_word) == 0:
        _tree.output = True
        return
    if _word[0] not in _tree.child:
        _tree.child[_word[0]] = node()
    return addTree(_tree.child[_word[0]], _word[1:])

for word in words:
    addTree(wordTree, word)

#방향 미리 설정
directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

def compWord(_tree,x,y,d,cnt=0,_word=""):
    if _tree.output:
        answer[_word] = (x,y,d)
        _tree.output = False
    if len(_tree.child)==0:
        return
    cx = x + directions[d][0] * cnt
    cy = y - directions[d][1] * cnt
    if cx < 0 or cx >= c or cy < 0 or cy >= l:
        return
    if board[cy][cx] not in _tree.child:
        return
    return compWord(_tree.child[board[cy][cx]],x,y,d,cnt+1,_word+board[cy][cx])


for i in range(l):
    for j in range(c):
        if board[i][j] in wordTree.child:
            for k in range(8):
                compWord(wordTree,j,i,k)

for word in words:
    y,x,d = answer[word]
    print(x,y,chr(d+65))