a = []
for _ in range(int(input())):
    s = input()
    a.append([len(s),sum([int(i) for i in s if i.isdigit()]),s])

a.sort(key=lambda x: (x[0],x[1],x[2]))

for i in a:
    print(i[2])