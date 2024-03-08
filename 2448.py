n = int(input())
def tri(c):
    if c == 3:
        r = ['  *  ',' * * ','*****']
        return r
    else:
        c//=2
        prev = tri(c)
        r = prev.copy()
        for i in range(c):
            r[i] = ' ' *c +r[i]+ ' ' * c
        for i in range(c):
            r.append(prev[i] +' '+prev[i])
        return r
    
print('\n'.join(tri(n)))
