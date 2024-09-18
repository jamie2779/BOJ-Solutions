import sys
t = map(int,sys.stdin.readlines())

for i in t:
    cnt = 1
    t = 1
    while t%i != 0:
        cnt += 1
        t *= 10
        t += 1
    print(cnt)
