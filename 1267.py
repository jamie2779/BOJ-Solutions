input()
t = map(int,input().split())
y=0
m=0
for i in t:
    y += i//30 +1
    m += i//60 +1
y*=10
m*=15
if (y<=m) : print('Y',end=' ')
if (m<=y) : print('M',end=' ')
print(min(y,m))