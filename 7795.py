import sys
input = sys.stdin.readline

for i in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    answer = 0
    p2 = 0
    for p1 in range(n):
        while p2<m:
            if a[p1] <= b[p2]:
                break
            p2+=1

        answer += p2  
    print(answer) 