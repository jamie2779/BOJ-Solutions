
m,n,o,p,q,r,s,t,u,v,w = map(int,input().split())
target = []
now = []
queue = []
next = []
ans = 0
for ww in range(w):
    for vv in range(v):
        for uu in range(u):
            for tt in range(t):
                for ss in range(s):
                    for rr in range(r):
                        for qq in range(q):
                            for pp in range(p):
                                for oo in range(o):
                                    for nn in range(n):
                                        a = input().split()
                                        for mm in range(m):
                                            if a[mm] == '1':
                                                next.append((ww,vv,uu,tt,ss,rr,qq,pp,oo,nn,mm))
                                            elif a[mm] == '0':
                                                target.append((ww,vv,uu,tt,ss,rr,qq,pp,oo,nn,mm))

while len(target) != len(now) and next:
    print(target,now,queue,next)
    while next:
        queue.append(next.pop())
    while queue:
        ww,vv,uu,tt,ss,rr,qq,pp,oo,nn,mm = queue.pop()
        for dw,dv,du,dt,ds,dr,dq,dp,do,dn,dm in [(1,0,0,0,0,0,0,0,0,0,0),(0,1,0,0,0,0,0,0,0,0,0),(0,0,1,0,0,0,0,0,0,0,0),(0,0,0,1,0,0,0,0,0,0,0),(0,0,0,0,1,0,0,0,0,0,0),(0,0,0,0,0,1,0,0,0,0,0),(0,0,0,0,0,0,1,0,0,0,0),(0,0,0,0,0,0,0,1,0,0,0),(0,0,0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,0,0,0,1)]:
            if (ww+dw,vv+dv,uu+du,tt+dt,ss+ds,rr+dr,qq+dq,pp+dp,oo+do,nn+dn,mm+dm) in target:
                now.append((ww+dw,vv+dv,uu+du,tt+dt,ss+ds,rr+dr,qq+dq,pp+dp,oo+do,nn+dn,mm+dm))
                next.append((ww+dw,vv+dv,uu+du,tt+dt,ss+ds,rr+dr,qq+dq,pp+dp,oo+do,nn+dn,mm+dm))
            if (ww-dw,vv-dv,uu-du,tt-dt,ss-ds,rr-dr,qq-dq,pp-dp,oo-do,nn-dn,mm-dm) in target:
                now.append((ww-dw,vv-dv,uu-du,tt-dt,ss-ds,rr-dr,qq-dq,pp-dp,oo-do,nn-dn,mm-dm))
                next.append((ww-dw,vv-dv,uu-du,tt-dt,ss-ds,rr-dr,qq-dq,pp-dp,oo-do,nn-dn,mm-dm))
    ans+=1
if len(target) != len(now):
    print(-1)
else:
    print(ans)