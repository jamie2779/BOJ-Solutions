c = input()
now = c[0]
count = 0
for i in c:
    if i != now:
        count += 1
        now = i
print((count+1)//2)