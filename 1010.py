#숫자가 커질수록 오차가 의미있게 되어서 아래 코드는 큰수에서 오류가 생기는듯함
for i in range(int(input())):
    n,m = map(int,input().split())
    r = 1
    for i in range(m,m-n,-1):
        r*=i
    for i in range(1,n+1):
        r/=i
    print(int(r))
#정답
for i in range(int(input())):
    n,m = map(int,input().split())
    r = 1
    for i in range(m,m-n,-1):
        r*=i
    for i in range(1,n+1):
        r//=i
    print(r)