def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def ext_gcd(a,b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = ext_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return g, x, y

def solve(a,b,s):
    if s<0:
        return False
    if a == 0 and b == 0:
        return s == 0
    if a == 0:
        return s%b == 0
    if b == 0:
        return s%a == 0
        
    g, x, y = ext_gcd(a, b)
    if s % g != 0:
        return False
    x *= s // g
    y *= s // g
    a //= g
    b //= g 

    k_min =0
    k_max = 0
    if b != 0:
        k_min = -x // b
    if a != 0:
        k_max = y // a

    for k in range(k_min, k_max + 1):
        if x + k * b >= 0 and y - k * a >= 0:
            if gcd(x + k * b, y - k * a) == 1:
                return True
    return False


a,b,s = map(int,input().split())

if solve(a,b,s):
    print("YES")
else:
    print("NO")