#2749번 응용
m = 1_000_000_007
f = [0,1]
n = int(input())
for i in range(2,n+1):
    f.append(f[i-1] + f[i-2])
    f[i] %= m

if n ==0:
    print(0)
else:
    print(f[-1])