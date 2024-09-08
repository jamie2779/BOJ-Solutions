import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    x1, y1 = points[i]
    x2, y2 = points[(i+1)%N]
    ans += (x1 * y2) - (x2*y1)

ans = abs(ans)/2

print(f"{ans:.1f}")