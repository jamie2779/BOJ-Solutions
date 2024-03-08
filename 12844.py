import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int,input().split()))
for i in range(int(input())):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        for j in range(cmd[1],cmd[2]+1):
            l[j] ^= cmd[3]
    else:
        total = l[cmd[1]]
        for j in range(cmd[1]+1,cmd[2]+1):
            total ^= l[j]
        print(total)