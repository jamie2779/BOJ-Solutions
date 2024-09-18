import sys
input = sys.stdin.readline
for i in range(int(input())):
    M, N, x, y = map(int,input().split())
    x -= 1
    y -= 1
    for i in range(x,M*N+1,M):
        if i%M == x and i%N == y:
            print(i+1)
            break
    else:
        print(-1)