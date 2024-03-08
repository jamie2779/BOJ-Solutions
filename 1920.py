#with.pypy3
input()
a = sorted(map(int,input().split()))
input()
t = map(int,input().split())
for i in t:
    print(int(i in a))
