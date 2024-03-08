import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = {}
    for _ in range(int(input())):
        n,m = input().split()
        if m in a:
            a[m].append(n)
        else:
            a[m] = [n]
    answer = 1
    for i in a.values():
        answer *= len(i)+1
    print(answer-1)