def culc(x,i):
    if x<i:
        return 0
    return ((x+1)//(i*2) * i) + max(((x+1)%(i*2))-i,0)

a,b = map(int,input().split())
total = 0
i = 1

while(i<b*2):
    mx = culc(b,i)
    mn = culc(a-1,i)
    total += mx-mn
    i*=2
print(total)