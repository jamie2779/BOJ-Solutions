n,m = map(int,input().split())
a = ['0'*(m+1)]+ ['0'+input() for _ in range(n)]
print(a)
b = [[min(map(int,(b[i-1][j-1], b[i][j-1],b[i-1][j])))+1 if a[i][j] != 0 else 0 for j in range(1,m+1)] for i in range(1,n+1)]
print(b)
print(max(map(max,b))**2)