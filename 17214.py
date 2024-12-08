ex = input()

num = [0,0]
if 'x' in ex:
    div = ex.split('x')
    num[0] = int(div[0])
    if div[1] != '':
        num[1] = int(div[1])
else:
    num[1] = int(ex)

num[0] //= 2

if num[0] != 0:
    if num[0] == -1:
        print("-",end='')
    if num[0] != 1 and num[0] != -1:
        print(num[0],end='')
    print('xx',end='')

if num[1] != 0:
    if num[0] != 0:
        if num[1] > 0:
            print('+',end='')
    if num[1] == -1:
        print('-',end='')
    if num[1] != 1 and num[1] != -1:
        print(num[1],end='')
    print('x',end='')

if num[0] != 0 or num[1] != 0:
    print('+',end='')
print('W')