n,m = map(int,input().split())
r,c,d = map(int,input().split())
floor = [[1]*m for _ in range(n)]
r1 = [list(map(int,input())) for _ in range(n)]
r2 = [list(map(int,input())) for _ in range(n)]
lr, lc, ld = r, c, d
lnum, lcount, count = 0, 0, 0 
while True:
    if r<0 or r>=n or c<0 or c>=m:
        break
    if floor[r][c] ==1:
        floor[r][c] = 0
        lr, lc, ld = r, c, d
        lcount = count+1
        d = (d+r1[r][c])%4
    else:
        if lr == r and lc == c and ld == d:
            if lnum == 0:
                lnum+=1
            else:
                break
        d = (d+r2[r][c])%4
    if d==0:
        r-=1
    elif d==1:
        c+=1
    elif d==2:
        r+=1
    else:
        c-=1
    count += 1

print(lcount)