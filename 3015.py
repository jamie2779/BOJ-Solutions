#시간초과
# import sys
# input = sys.stdin.readline
# n = int(input())

# a = []
# for i in range(n):
#     a.append(int(input().strip()))
 
# cnt = 0
# for i in range(n-1):
#     m = 0
#     for j in range(i+1,n):
#         if a[j]>=m and m<=a[i]:
#             cnt += 1
#             m = a[j]
#         elif m>a[i]:
#             break
            
# print(cnt)

a = [int(input()) for _ in range(int(input()))]

s = []
cnt = 0

for i in a:
    while len(s)>0 and s[-1][0]<i:
        cnt += s.pop()[1]
    
    if len(s) == 0:
        s.append((i,1))
        continue

    if s[-1][0] == i:
        c = s.pop()[1]
        cnt += c

        if len(s) > 0:
            cnt += 1
        s.append((i,c+1))

    else:
        s.append((i,1))
        cnt+=1

print(cnt)