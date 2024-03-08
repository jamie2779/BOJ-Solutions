n = int(input())
a = [int(input()) for _ in range(n)]

st = []
cmd = []
idx = 0
next = 1

while idx <len(a):
    if next <= a[idx]:
        st.append(next)
        cmd.append('+')
        next +=1
    elif st[-1] == a[idx]:
        st.pop()
        cmd.append('-')
        idx += 1
    else:
        cmd = ['NO']
        break
        
print('\n'.join(cmd))
