import re
p = re.compile('(100+1+|01)+')
n = int(input())
for i in range(n):
    s = input()
    m = p.fullmatch(s)
    if m:
        print("YES")
    else:
        print("NO")