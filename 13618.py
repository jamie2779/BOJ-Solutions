def eq(a, b):
    x,g,v,w = 1, a, 0, b
    while True:
        if w == 0:
            while(x<0):
                x += b
            return x
        q = g // w
        t = g % w
        s = x - q * v
        x, g = v, w
        v, w = s, t


n,e,c = map(int,input().split())

p=0
q=0
for i in range(2,n-1):
    if n%i == 0:
        p = i
        q = n//i
        break

phi = (p-1)*(q-1)
u = eq(e,phi)
print(pow(c,u,n))

