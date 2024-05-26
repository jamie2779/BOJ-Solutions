import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int,input().split())
chicken = []
home = []
cnt = {}

for i in range(n):   #입력받은 값을 바탕으로 home 좌표 배열과 chicken 좌표 배열 저장
    line = input().split()
    for j in range(n):
        if line[j] == '1':
            home.append((i,j))
        elif line[j] == '2':
            chicken.append((i,j))
            cnt[(i,j)] = 0

#
for h_pos in home:   #각 치킨집에 대하여 최솟값 계산에 몇번 쓰였는지 카운트
    minIdx = 0
    minVal = 2*n
    for j in range(len(chicken)):
        c_pos = chicken[j]
        d = abs(h_pos[0] - c_pos[0]) + abs(h_pos[1] - c_pos[1])
        if d < minVal:
            minVal = d
            minIdx = j
    cnt[chicken[minIdx]] += 1

cnt_sort = list(cnt.items())       #카운트 한 값을 바탕으로 정렬
cnt_sort.sort(key = lambda x: x[1], reverse=True)

fixed_target = []
random_target = []                  # m개를 뽑아야 하는데 m을 넘으면서 숫자가 바뀌는 부분 찾기
last_cnt = cnt_sort[0][1]           # ex) 5 4 4 3 3 3 3 인데 5개인 경우 어떤 3이 될지 모르므로 5 4 4 까지는 fixed, 나머지 3이 나오는 좌표는 다 해봐야 하므로 random에 넣어둠
cnt = 0                             
for i in cnt_sort:
    if i[1] == last_cnt:
        random_target.append(i[0])
        cnt += 1
    else:
        if cnt>m:
            break
        fixed_target += random_target
        random_target = []
        last_cnt = i[1]
        if  cnt == m:
            break
        random_target.append(i[0])
        cnt += 1

def culDistence(target):        #target의 치킨집 좌표를 바탕으로 치킨거리 구하는 함수
    res = 0
    for h_pos in home:
        minVal = 2*n
        for c_pos in target:
            d = abs(h_pos[0] - c_pos[0]) + abs(h_pos[1] - c_pos[1])
            if d < minVal:
                minVal = d
        res += minVal
    return res

comb = combinations(random_target, m-len(fixed_target))         #random_target 의 모든 조합을 구해서 각 조합에 따른 치킨거리 구하고 최솟값 출력
ans = []
for i in comb:
    ans.append(culDistence(fixed_target+list(i)))
print(min(ans))