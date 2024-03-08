def listap(l,p,a,b):
    for i in range(len(p)):
        for j in range(len(p[0])):
            l[i+a][j+b] = p[i][j]
            
            
    return l

def st(a):
    if a ==1:
        return [['*']]
    else:
        n = []
        for p in range(a):
            n.append([' ']*a)
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    n = listap(n,st(a//3),a//3*i,a//3*j)
    return n
t = st(int(input()))
for i in range(len(t)):
    print(''.join(t[i]))	