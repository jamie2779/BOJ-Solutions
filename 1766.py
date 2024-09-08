import sys
input = sys.stdin.readline

from collections import defaultdict
import heapq

n, m = map(int,input().split())

rule = defaultdict(list)
cnt = [0] * (n+1)

for i in range(m):
    a,b = map(int,input().split())
    rule[a].append(b)
    cnt[b] += 1

queue = []
for i in range(1,n+1):
    if cnt[i] == 0:
        heapq.heappush(queue,i)

while queue:
    now = heapq.heappop(queue)
    print(now, end =' ')
    for j in rule[now]:
        cnt[j] -= 1
        if cnt[j] == 0:
            heapq.heappush(queue,j)
