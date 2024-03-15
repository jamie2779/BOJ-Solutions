a, b, c = map(int,input().split())

def pow(a,b):
    if b == 1:
        return a
    if b%2==0:
        res = pow(a,b/2)**2
    else:
        res = pow(a,b//2)**2*a
    return res%c

a%=c
print(pow(a,b))