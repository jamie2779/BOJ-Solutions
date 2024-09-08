#드디어시작이다 RPG Extreme
import sys
input = sys.stdin.readline

class Monster:
    def __init__(self,name, attack, defense, health, exp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.exp = exp
    
class Chest:
    def __init__(self, type, info):
        self.type = type
        self.info = info

class Player:
    def __init__(self,r, c):
        self.init_pos = (r,c)
        self.cur_pos = (r,c)
        self.max_health = 20
        self.health = 20
        self.attack = 2
        self.defense = 2
        self.level = 1
        self.cur_exp = 0
        self.max_exp = 5
        self.weapon = 0
        self.armor = 0
        self.last_attack = ""
        #0:HR, 1:RE, 2:CO, 3:EX, 4:DX, 5:HU, 6:CU
        self.accessories = set()
    
    #피해 입는거 처리(고정피해)
    def hurt(self, amount, attacker):
        self.last_attack = attacker
        self.health -= amount
        if self.health < 0:
            self.health = 0
        
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
    
    def getExp(self, amount):
        self.cur_exp += amount
        #레벨업
        if self.cur_exp >= self.max_exp:
            self.cur_exp = 0
            self.level += 1
            self.max_exp = self.level * 5
            self.max_health += 5
            self.attack += 2
            self.defense += 2
            self.health = self.max_health


    def fight(self, monster: Monster,isBoss:bool = False):
        monster_health = monster.health
        first_attack = 1
        boss_attack = False
        
        #HU 장신구 처리
        if isBoss and "HU" in self.accessories:
            player.health = player.max_health
            boss_attack = True

        #CO 장신구 처리
        if "CO" in self.accessories:
            first_attack += 1
            #DX 장신구 처리
            if "DX" in self.accessories:
                first_attack += 1
        while True:
            monster_health -= max(1,(self.attack + self.weapon)*first_attack - monster.defense)
            if monster_health <= 0:
                exp = monster.exp
                #EX 장신구 처리
                if "EX" in self.accessories:
                    exp = int(exp * 1.2)
                player.getExp(exp)
                #HR 장신구 처리
                if "HR" in self.accessories:
                    self.heal(3)
                return True
            if boss_attack:
                boss_attack = False
            else:
                self.hurt(max(1,monster.attack - (self.defense + self.armor)), monster.name)
                if self.health == 0:
                    return False
            first_attack = 1

turn = 0
player = None
monster_cnt = 0
chest_cnt = 0
monsters = {}
chests = {}

#보드 입력
n, m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]

#보드 정보 추출(플레이어위치, 몬스터 개수, 상자 개수)
for i in range(n):
    for j in range(m):
        if board[i][j] == '@':
            player = Player(i,j)
            board[i][j] ='.'
        elif board[i][j] == '&' or board[i][j] == 'M':
            monster_cnt += 1
        elif board[i][j] == 'B':
            chest_cnt += 1

#커맨드 입력
command = list(input().strip()[::-1])

#몬스터 정보 입력
for i in range(monster_cnt):
    r,c,s,w,a,h,e = input().split()
    r,c,w,a,h,e = map(int,(r,c,w,a,h,e))
    monsters[(r-1,c-1)] = Monster(s,w,a,h,e)

#상자 정보 입력
for i in range(chest_cnt):
    r,c,t,s = input().split()
    r, c = map(int,(r,c))
    if t != 'O':
        s = int(s)
    chests[(r-1,c-1)] = Chest(t,s)

#턴 진행
while command:
    turn += 1
    now = command.pop()

    #이동
    target_r, target_c = player.cur_pos
    if now == 'U':
        target_r -= 1
    elif now == 'D':
        target_r += 1
    elif now == 'L':
        target_c -= 1
    else:
        target_c += 1
    
    if 0 <= target_r and target_r < n and 0 <= target_c and target_c < m and board[target_r][target_c] != '#':
        player.cur_pos = (target_r, target_c)

    # 아이템 상자
    cur_r, cur_c = player.cur_pos
    if board[cur_r][cur_c] == 'B':
        board[cur_r][cur_c] = '.'
        cur_chest = chests[(cur_r, cur_c)]
        if cur_chest.type == 'W':
            player.weapon = cur_chest.info
        elif cur_chest.type == 'A':
            player.armor = cur_chest.info
        elif len(player.accessories) <4:
            player.accessories.add(cur_chest.info)

    
    #가시함정
    elif board[cur_r][cur_c] == '^':
        #DX 장신구 처리
        if "DX" in player.accessories:
            player.hurt(1,"SPIKE TRAP")
        else:
            player.hurt(5,"SPIKE TRAP")
    
    #몬스터 전투
    elif board[cur_r][cur_c] == '&':
        if player.fight(monsters[(cur_r,cur_c)]):
            board[cur_r][cur_c] = '.'

    #보스 전투
    elif board[cur_r][cur_c] == 'M':
        if player.fight(monsters[(cur_r,cur_c)],True):
            board[cur_r][cur_c] = '.'
            command=["CLEAR!!!"]
            break

    if player.health == 0:
        #RE 장신구 처리
        if "RE" in player.accessories:
            player.accessories.remove("RE")
            player.health = player.max_health
            player.cur_pos = player.init_pos
        else:
            break

if player.health > 0:
    r,c = player.cur_pos
    board[r][c] = '@'

for i in board:
    print("".join(i))

print(f"Passed Turns : {turn}")
print(f"LV : {player.level}")
print(f"HP : {player.health}/{player.max_health}")
print(f"ATT : {player.attack}+{player.weapon}")
print(f"DEF : {player.defense}+{player.armor}")
print(f"EXP : {player.cur_exp}/{player.max_exp}")

if player.health == 0:
    print(f"YOU HAVE BEEN KILLED BY {player.last_attack}..")
elif command:
    print("YOU WIN!")
else:
    print("Press any key to continue.")

