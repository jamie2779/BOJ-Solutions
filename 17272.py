p = 1000000007
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

n,m = map(int,input().split())
mat = [[1 if i+1 == j else 0 for i in range(m)] for j in range(m)]
mat[0][0] = 1
mat[0][-1] = 1


res = mat_pow(mat,n)

print(res[0][0])
