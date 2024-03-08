for _ in range(int(input())):
    n,m = map(int,input().split())
    d = list(map(int,input().split()))
    cnt = 0
    while True:
        if max(d) == d[0]:
            cnt += 1
            if m == 0:
                print(cnt)
                break
            m-=1
            d.pop(0)
        else:
            d.append(d[0])
            d.pop(0)
            if m == 0:
                m = len(d)-1
            else:
                m-=1