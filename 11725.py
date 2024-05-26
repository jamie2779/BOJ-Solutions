n= int(input())
node= [[] for i in range(n+1)]
ans= [1,1]+[-1]*(n-1)

for i in range(n-1):
    b,c = map(int,input().split())
    node[b].append(c)
    node[c].append(b)

stack = [1]

while stack:
    k = stack.pop()
    for i in node[k]:
        if ans[i] == -1:
            ans[i] = k
            stack.append(i)

for i in ans[2:]:
    print(i)