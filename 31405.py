n = int(input())
#점 받기
pos = [tuple(map(int,input().split())) for _ in range(n)]

#누적합 계산
s = [0]
for i in range(1,n-1):    
    area = pos[0][0] * pos[i][1] + pos[i][0] * pos[i+1][1] + pos[i+1][0]*pos[0][1] - pos[i][0] * pos[0][1] - pos[i+1][0] * pos[i][1] - pos[0][0] * pos[i+1][1]
    area = abs(area)
    area *= 0.5
    s.append(s[-1]+area)

#절반 넓이
target = s[-1]/2

print("YES")
print("1 0")

#나머지 점
for i in range(0,n-1):
    if s[i]<=target and s[i+1]>target:
        print(f"{i+2} {(target - s[i]) /(s[i+1] - s[i]):.12f}")