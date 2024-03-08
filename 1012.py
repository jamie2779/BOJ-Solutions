import sys
input = sys.stdin.readline
for _t in range(int(input())):
    m,n,k = map(int,input().split())
    r = []
    for _k in range(k):
        r.append(input().strip())
    cnt = 0    
    while len(r)>0:
        cnt += 1
        a=[r[0]]
        while len(a)>0:
            k = a.pop()
            if k in r:
                r.remove(k)
                x,y = map(int,k.split())
                a.append(f'{x-1} {y}')     
                a.append(f'{x+1} {y}')       
                a.append(f'{x} {y-1}')       
                a.append(f'{x} {y+1}')
    print(cnt)       

