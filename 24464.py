a = [[1,1,1,1,1]]
n = int(input())
M = 1_000_000_007
for i in range(n-1):
    line = [0,0,0,0,0]
    last = a[i]
    line[0] = (last[1] + last[2] + last[3] + last[4]) % M
    line[1] = (last[0] + last[3] + last[4]) % M
    line[2] = (last[0] + last[4]) % M
    line[3] = (last[0] + last[1]) % M
    line[4] = (last[0] + last[1] + last[2]) % M
    a.append(line)
print(sum(a[-1])%M)