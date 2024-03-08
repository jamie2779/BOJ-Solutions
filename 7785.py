now = {}
for _ in range(int(input())):
    n, c = input().split()
    now[n] = c
print("\n".join(sorted([n for n,v in now.items() if v=="enter"],reverse=True)))