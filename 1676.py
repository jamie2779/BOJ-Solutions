n = int(input())

c = 1
for i in range(2,n+1):
    c *= i

cnt = 0
while True:
    if c%10 != 0:
        break
    else:
        cnt +=1
        c//=10
print(cnt)