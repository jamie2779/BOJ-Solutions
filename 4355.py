while True:
    n = int(input())
    if n == 0:
        break

    if n == 1:
        print(0)
        continue
        
    res = n
    i = 2
    while i * i <= n:
        cnt = 0
        while n%i == 0:
            n//=i
            cnt += 1
        if cnt > 0:
            res *= (1-1/i)
        i+=1
    
    if n>1:
        res *= (1-1/n)
    
    print(int(res))