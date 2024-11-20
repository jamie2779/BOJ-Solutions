n,m = input().split()

if len(n) != len(m):
    print(0)
else:
    res = 0
    for i in range(len(n)):
        if n[i] == '8' and m[i] == '8':
            res+=1
        elif n[i] != m[i]:
            break
        
    print(res)
