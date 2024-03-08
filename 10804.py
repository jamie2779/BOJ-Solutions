c = list(range(0,21))
for i in range(10):
    a,b = map(int,input().split())
    c[a:b+1] = c[b:a-1:-1]
print(" ".join(map(str,c[1:])))