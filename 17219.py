import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
d = {}
for i in range(n):
    s,p = input().strip().split()
    d[s] = p
for i in range(m):
    print(d[input()])