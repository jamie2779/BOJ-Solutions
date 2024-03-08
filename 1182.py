import itertools as it
n,s = map(int,input().split())
l = input().split()
cnt = 0
for i in range(1,n+1):
    for c in it.combinations(l,i):
        if sum(map(int,c)) == s:
            cnt+=1
print(cnt)
