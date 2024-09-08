import sys
input = sys.stdin.readline
st = [""]
time = [0]
for _ in range(int(input())):
    cmd = input().split()
    t = int(cmd[2])
    if cmd[0] == 'type':
        st.append(st[-1] + cmd[1])
        
    else:
        past = t - int(cmd[1])
        i = len(st)-1
        while time[i] > 0 and time[i] >= past:
            i-=1
        st.append(st[i])
    time.append(t)

print(st[-1])