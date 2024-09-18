import sys
input = sys.stdin.readline
for i in range(int(input())):
    num = map(int,input().split())
    num.sort()
    print(num[-3])