#insert 사용으로 시간초과 발생 -> stack 사용 고려
a = list(input())
l = len(a)
cu = l
for i in range(int(input())):
    cmd = input()
    if cmd[0] == 'L':
        cu = max(0,cu-1)
    elif cmd[0] == 'D':
        cu = min(cu+1,l)
    elif cmd[0] =='B':
        if cu>0:
            del a[cu-1]
            cu-=1
            l-=1
    else:
        a.insert(cu,cmd[2])
        cu+=1
        l+=1
print(''.join(a))
