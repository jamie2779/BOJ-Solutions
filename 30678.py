def star(n):
    if n == 0:
        return ['*']
    else:
        prev = star(n-1)
        res = [" "*(5**n) for _ in range(5**n)]
        l = len(prev)
        mask = ((0,0,1,0,0),(0,0,1,0,0),(1,1,1,1,1),(0,1,1,1,0),(0,1,0,1,0))

        for i in range(5):
            for j in range(5):
                if mask[i][j] == 1:
                    r = i*l
                    c = j*l
                    for k in range(l):
                        res[r+k] = res[r+k][:c] + prev[k] + res[r+k][c+l:]
        return res

n = int(input())

for i in star(n):
    print(i)
