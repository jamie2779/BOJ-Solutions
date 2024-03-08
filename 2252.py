#시간초과 남 수정요망
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
nlist = [[] for _ in range(n)]
check = list(range(n))
line = []
for i in range(m):
    a,b = map(int,input().split())
    nlist[b-1].append(a-1)

while len(check)>0:
    for i in check:
        if len(nlist[i]) == 0:
            line.append(i+1)
            for j in check:
                if i in nlist[j]:
                    nlist[j].remove(i)
            check.remove(i)
print(*line)