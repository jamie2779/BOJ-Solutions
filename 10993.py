def star(n):
    blank = 2*(2**(n-1)-1)
    st = 2*blank + 1
    res = []
    if n == 1:
        res = ['*']
    elif n%2==0:
        res.append(["*"]*st)
        for i in range(1,blank-1):
            res.append(list(' ' * i +'*'+ ' '))
        res.append(list(" "*blank + "*" + " "*blank))
            


    for i in res:
        print(i)

star(2)
print()
star(4)
