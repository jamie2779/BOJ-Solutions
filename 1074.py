def f(n,r,c):
    if n == 1:
        return 2*r+c
    else:
        n-=1
        quad = 2*(r//(2**n))+(c//(2**n)) #사분면의 위치를 나타낸다, 0,1,2,3 중 하나
        return (4**n)*quad + f(n,r%(2**n),c%(2**n))

n, r, c = map(int,input().split())
print(f(n,r,c))