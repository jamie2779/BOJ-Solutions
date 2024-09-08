n = int(input())
mask = [True] * (n+1)
p = []
for i in range(2,n+1):
    if mask[i]:
        p.append(i)
        for j in range(i*i,n+1,i):
            mask[j] = False
        
p1 = 0
p2 = 0

cnt = 0
s = 0
while p2 < len(p) or s>=n:
    if s < n :
        s += p[p2]
        p2+=1
    elif s>n:
        s -= p[p1]
        p1+=1
    else:
        cnt += 1
        if p2 == len(p):
            break
        s += p[p2]
        p2+=1

print(cnt)
