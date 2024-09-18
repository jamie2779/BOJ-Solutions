from itertools import combinations
l, c = map(int,input().split())
target = input().split()
target.sort()
info = [0] * c

for i in range(c):
    if target[i] in 'aeiou':
        info[i] = 1;

for i in combinations(range(c),l):
    s = 0
    txt = ''
    for j in i:
        s+=info[j]
        txt += target[j]
    if s>=1 and l-s >=2:
        print(txt) 