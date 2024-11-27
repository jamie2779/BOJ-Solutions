n = int(input())
cnt = 2**n -1
print(cnt)

def solve (st, en, cnt):
    if cnt == 1:
        print(st, en)
    else:
        mi = 6 - st - en
        solve(st,mi,cnt-1)
        print(st, en)
        solve(mi,en,cnt-1)
    
if n <= 20:
    solve(1,3,n)