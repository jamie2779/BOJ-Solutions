e,s,m = map(int,input().split())
e-=1
s-=1
m-=1
for i in range(8000):
    if i%15 == e and i%28 == s and i%19 == m:
        print(i+1)
        break