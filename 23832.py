n = int(input())

def phi(n):
    res = n

    i = 2
    while i * i <= n:
        cnt = 0
        while n%i == 0:
            n//=i
            cnt += 1
        if cnt > 0:
            res *= (1-1/i)
        i+=1

    if n>1:
        res *= (1-1/n)
    return int(res)

answer = 0
for i in range(2,n+1):
    answer += phi(i)
print(answer)
