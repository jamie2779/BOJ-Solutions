import sys
input = sys.stdin.readline
t = int(input())
sides = {'U':0,'L':1,'F':2,'R':3,'B':4,'D':5}
def turn(code):
    side = sides[code[0]]
    direction = code[1]
    for i in range(1 if direction == '-' else 3):
        for j in range(2):
            #해당 면 돌리기
            temp = cube[side][0][0]
            cube[side][0][0] = cube[side][0][1]
            cube[side][0][1] = cube[side][0][2]
            cube[side][0][2] = cube[side][1][2]
            cube[side][1][2] = cube[side][2][2]
            cube[side][2][2] = cube[side][2][1]
            cube[side][2][1] = cube[side][2][0]
            cube[side][2][0] = cube[side][1][0]
            cube[side][1][0] = temp
        for j in range(3):
            #옆면 돌리기
            if side ==0:
                temp = cube[4][0][2]
                cube[4][0][2] = cube[4][0][1]
                cube[4][0][1] = cube[4][0][0]
                cube[4][0][0] = cube[3][0][2]
                cube[3][0][2] = cube[3][0][1]
                cube[3][0][1] = cube[3][0][0]
                cube[3][0][0] = cube[2][0][2]
                cube[2][0][2] = cube[2][0][1]
                cube[2][0][1] = cube[2][0][0]
                cube[2][0][0] = cube[1][0][2]
                cube[1][0][2] = cube[1][0][1]
                cube[1][0][1] = cube[1][0][0]
                cube[1][0][0] = temp
            elif side ==1:
                temp = cube[0][0][0]
                cube[0][0][0] = cube[0][1][0]
                cube[0][1][0] = cube[0][2][0]
                cube[0][2][0] = cube[2][0][0]
                cube[2][0][0] = cube[2][1][0]
                cube[2][1][0] = cube[2][2][0]
                cube[2][2][0] = cube[5][0][0]
                cube[5][0][0] = cube[5][1][0]
                cube[5][1][0] = cube[5][2][0]
                cube[5][2][0] = cube[4][2][2]
                cube[4][2][2] = cube[4][1][2]
                cube[4][1][2] = cube[4][0][2]
                cube[4][0][2] = temp
            elif side ==2:
                temp = cube[0][2][0]
                cube[0][2][0] = cube[0][2][1]
                cube[0][2][1] = cube[0][2][2]
                cube[0][2][2] = cube[3][0][0]
                cube[3][0][0] = cube[3][1][0]
                cube[3][1][0] = cube[3][2][0]
                cube[3][2][0] = cube[5][0][2]
                cube[5][0][2] = cube[5][0][1]
                cube[5][0][1] = cube[5][0][0]
                cube[5][0][0] = cube[1][2][2]
                cube[1][2][2] = cube[1][1][2]
                cube[1][1][2] = cube[1][0][2]
                cube[1][0][2] = temp
            elif side ==3:
                temp = cube[0][2][2]
                cube[0][2][2] = cube[0][1][2]
                cube[0][1][2] = cube[0][0][2]
                cube[0][0][2] = cube[4][0][0]
                cube[4][0][0] = cube[4][1][0]
                cube[4][1][0] = cube[4][2][0]
                cube[4][2][0] = cube[5][2][2]
                cube[5][2][2] = cube[5][1][2]
                cube[5][1][2] = cube[5][0][2]
                cube[5][0][2] = cube[2][2][2]
                cube[2][2][2] = cube[2][1][2]
                cube[2][1][2] = cube[2][0][2]
                cube[2][0][2] = temp
            elif side ==4:
                temp = cube[0][0][2]
                cube[0][0][2] = cube[0][0][1]
                cube[0][0][1] = cube[0][0][0]
                cube[0][0][0] = cube[1][0][0]
                cube[1][0][0] = cube[1][1][0]
                cube[1][1][0] = cube[1][2][0]
                cube[1][2][0] = cube[5][2][0]
                cube[5][2][0] = cube[5][2][1]
                cube[5][2][1] = cube[5][2][2]
                cube[5][2][2] = cube[3][2][2]
                cube[3][2][2] = cube[3][1][2]
                cube[3][1][2] = cube[3][0][2]
                cube[3][0][2] = temp
            elif side ==5:
                temp = cube[1][2][0]
                cube[1][2][0] = cube[1][2][1]
                cube[1][2][1] = cube[1][2][2]
                cube[1][2][2] = cube[2][2][0]
                cube[2][2][0] = cube[2][2][1]
                cube[2][2][1] = cube[2][2][2]
                cube[2][2][2] = cube[3][2][0]
                cube[3][2][0] = cube[3][2][1]
                cube[3][2][1] = cube[3][2][2]
                cube[3][2][2] = cube[4][2][0]
                cube[4][2][0] = cube[4][2][1]
                cube[4][2][1] = cube[4][2][2]
                cube[4][2][2] = temp
    
for testcase in range(t):
    n = int(input())
    turns = input().split()
    cube = [
        [['w','w','w'],
         ['w','w','w'],
         ['w','w','w']],
        [['g','g','g'],
         ['g','g','g'],
         ['g','g','g']],
        [['r','r','r'],
         ['r','r','r'],
         ['r','r','r']],
        [['b','b','b'],
         ['b','b','b'],
         ['b','b','b']],
        [['o','o','o'],
         ['o','o','o'],
         ['o','o','o']],
        [['y','y','y'],
         ['y','y','y'],
         ['y','y','y']]
        ]
    for t in turns:
        turn(t)
    print(*cube[0][0],sep='')
    print(*cube[0][1],sep='')
    print(*cube[0][2],sep='')
