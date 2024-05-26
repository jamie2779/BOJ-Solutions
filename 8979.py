n, k = map(int,input().split())
a = []
b = {}
for i in range(n):
    n, g, s, b = map(int,input().split())
    b[n] = tuple([g, s, b])
    a.append((g,s,b))
a = list(set(a))
a.sort(key=lambda x: (x[1],x[2],x[3]), reverse=True)

print(a)
cnt = 0
for i in a:       
    cnt += 1
    if i == b[k]:
        print(cnt) 
        break
    