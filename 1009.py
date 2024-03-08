for i in range(int(input())):
    a,b = map(int,input().split())
    k =pow(a,b,10)
    if k == 0:
        print(10)
    else:
        print(k)