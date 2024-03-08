import sys
input = sys.stdin.readline
s = set()
for i in range(int(input())):
    cmd = input().strip().split()
    if cmd[0] == 'add':
        s.add(cmd[1])
    elif cmd[0] == 'remove':
        if cmd[1] in s:
            s.remove(cmd[1])
    elif cmd[0] == 'check':
        if cmd[1] in s:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if cmd[1] in s:
            s.remove(cmd[1])
        else:
            s.add(cmd[1])
    elif cmd[0] == 'all':
        s = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    elif cmd[0] == 'empty':
        s = set()
