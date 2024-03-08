# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# d = [input().strip() for _ in range(n)]
# for i in [input().strip() for _ in range(m)]:
#     if i.isdigit():
#         print(d[int(i)-1])
#     else:
#         print(d.index(i)+1)
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
d1={}
d2={}
for i in range(1,n+1):
    name = input().strip()
    d1[str(i)] = name
    d2[name] = i
for i in range(m):
    t = input().strip()
    if t.isdigit():
        print(d1[t])
    else:
        print(d2[t])