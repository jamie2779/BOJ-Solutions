decimal = input()
up = 1
down = 1
if '.' not in decimal:
    up = int(decimal)
else:
    a, b = decimal.split('.')
    
    if '(' not in b:
        up = int(f'{a}{b}')
        down = 10 ** len(b)
    else:
        n, r = b.split('(')
        r = r[:-1]
        up = int(f'{a}{n}{r}') - int(f'{a}{n}')
        down = int('9'*len(r)+'0'*len(n))

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

g = gcd(up,down)
print(f'{up//g}/{down//g}')
