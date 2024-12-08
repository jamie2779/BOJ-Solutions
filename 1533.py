p = 1000003
def mat_mul(a,b):
    res = [[0 for _ in range(len(a[0]))]for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(a)):
                res[i][j] += a[i][k] * b[k][j]
                res[i][j] %=p
    return res

def mat_pow(a,n):
    res = [[1 if i== j else 0 for i in range(len(a))] for j in range(len(a))]
    while n>0:
        if n % 2 == 1:
            res = mat_mul(res,a)
        a = mat_mul(a,a)
        n//=2
    return res


n,s,e,t = map(int,input().split())
time = []
for i in range(n):
    time.append(list(map(int,input())))

mat = [[0 for _ in range(50)]for _ in range(50)]

for i in range(50):
    if i % 5 > 0:        
        mat[i][i-1] = 1

now = n 
for i in range(n):
    for j in range(n):
        if time[i][j]>0:
            mat[5 * i][5*j+time[i][j]-1] = 1

target = mat_pow(mat,t)
print(target[(s-1)*5][(e-1)*5])
