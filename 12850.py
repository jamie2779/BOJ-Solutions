# 정 전 미 신 한 진 형 학
mat = [[0,1,1,0,0,0,0,0],
       [1,0,1,1,0,0,0,0],
       [1,1,0,1,1,0,0,0],
       [0,1,1,0,1,1,0,0],
       [0,0,1,1,0,1,1,0],
       [0,0,0,1,1,0,0,1],
       [0,0,0,0,1,0,0,1],
       [0,0,0,0,0,1,1,0]]

mod = 1000000007

d = int(input())

def mat_mul(m1, m2):
    res = [[0 for i in range(8)] for i in range(8)]
    for i in range(8):
        for j in range(8):
            s = 0
            for k in range(8):
                s += m1[i][k] * m2[k][j]
                s %= mod
            res[i][j] = s%mod
    return res

res = [[1 if i==j else 0 for i in range(8)]for j in range(8)]

while d>0:
    if d%2 == 1:
        res = mat_mul(res,mat)
    mat = mat_mul(mat , mat)
    d//=2

print(res[0][0])