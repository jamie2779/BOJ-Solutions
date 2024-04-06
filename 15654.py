from itertools import permutations
a, b = map(int,input().split())
c = sorted(list(map(int,input().split())))

for i in permutations(c,b):
    print(*i)