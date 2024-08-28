#해시를 이용한 집합과 맵, 정렬, 투포인터 비스무리하게 사용해서 해결
n = int(input())
card = list(map(int,input().split()))
card.sort()
m = int(input())
target = list(map(int,input().split()))

ans = {}

p = 0
for i in sorted(target):
    while True:
        if card[p] == i:
            ans[i] = 1
            break
        elif card[p]> i or p == n-1:
            ans[i] = 0
            break
        else:
            p+=1

for i in target:
    print(ans[i],end=" ")

