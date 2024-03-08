# #가장 단순한 풀이법 - 시간초과 오답
# k,n = map(int,input().split())
# l = [int(input()) for _ in range(k)]

# m= 0
# for i in range(1,max(l)+1):
#     cnt = 0
#     for j in l:
#         cnt += j//i
#     if cnt >= n:
#         m = i
# print(m)

#이분탐색 활용 - 정답
k,n = map(int,input().split())
l = [int(input()) for _ in range(k)]

start, end = 1, max(l)+1
while True:
    if end - start <2:
        break

    mid = start + (end - start)//2   
    cnt = 0
    for j in l:
        cnt += j//mid

    if cnt >= n:
        start = mid
    else:
        end = mid
print(start)