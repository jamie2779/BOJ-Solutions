s = input()
target = "KOREA"
now = 0
cnt = 0

for c in s:
    if c == target[now]:
        now += 1
        now %=5
        cnt += 1

print(cnt)