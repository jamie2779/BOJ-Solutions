a,b,c=map(int,input().split())
if c-a>=0:
    if b>c:
        print('Subway')
    elif b==c:
        print('Anything')
    else:
        print('Bus')
else:
    print('Bus')