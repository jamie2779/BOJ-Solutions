m = int(input())
def binomial(n,k):
    res = 1
    for i in range(1,k+1):
        res *= n-(i-1)
        res//=i
    return res

ans = []
for i in range(1,32):
    start = i*2
    end = m+1
    while start+1<end:
        mid = (start+end)//2
        bi = binomial(mid,i)
        if bi<=m: 
            start = mid
        else:
            end = mid
    if binomial(start,i) == m:
        ans.append((start,i))
        if i<start-i:
            ans.append((start,start-i))

ans.sort()

print(len(ans))
for i,j in ans:
    print(i,j)