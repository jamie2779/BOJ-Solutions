from itertools import permutations
a, b = map(int,input().split())
c = list(map(int,input().split()))

res = list(set(permutations(c,b)))
for i in range(1,b+1):
    res.sort(key=lambda x: x[-i])

for i in res:
    print(*i)