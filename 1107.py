while True:
    n = input()
    m = int(input())
    if(m>0):
        b = input().split()

    res = abs(100-int(n))
    if m == 0 or set(n).isdisjoint(set(b)): #필요한 숫자를 다 누를 수 있을 때
        res = min(res,len(n))
    else:
        cb = {'0','1','2','3','4','5','6','7','8','9'} - set(b)
        maxb = max(cb)
        minb = min(cb)

        #n보다 크면서 가까운 수 비교
        c = True
        num = ''
        for i in n:
            if c and i not in b:
                num+=i
            elif c:
                c = False
                for j in range(int(i)+1,10):
                    if str(j) not in b:
                        num += str(j)
                        break
                else:
                    break
            else:
                num+=minb
        else:
            res = min(res, len(n) + abs(int(num) - int(n)))
        
        #n보다 작으면서 가까운 수 비교
        c = True
        num = ''
        for i in n:
            if c and i not in b:
                num+=i
            elif c:
                c = False
                for j in range(int(i)-1,-1,-1):
                    if sa r(j) not in b:
                        num += str(j)
                        break
                else:
                    break
            else:
                num+=maxb
        else:
            res = min(res, len(n) + abs(int(num) - int(n)))
        
    print(res)