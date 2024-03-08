from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    reverse = False
    cmd = input().strip()
    n = int(input())
    #리스트 파싱
    r = input().strip()
    if len(r) == 2:
        lst = []
    else:
        lst = deque(map(int,r[1:-1].split(",")))
    for c in cmd:
        if c == "R":
            reverse = False if reverse else True
        if c == "D":
            if len(lst) == 0:
                print("error")
                break
            else:
                lst.pop() if reverse else lst.popleft()
    else:
        if reverse:
            lst.reverse()
        print('[', end="")
        print(",".join(map(str,lst)),end="")
        print(']')
