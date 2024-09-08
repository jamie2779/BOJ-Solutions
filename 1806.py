n,s = map(int,input().split())
a = list(map(int,input().split()))

if sum(a) < s:
    print(0)
else:
    p1 = 0
    p2 = 0
    res = n
    cur = 0
    while True:
        if cur >=s:
            res = min(res,p2-p1)
            cur -= a[p1]
            p1+=1
        elif p2 == n:
            break
        else:
            cur += a[p2]
            p2+=1
    print(res)