n, k = map(int,input().split())

medal = []
rank = [1]

for i in range(n):
    medal.append(list(map(int,input().split())))

medal.sort(key= lambda x: -x[3])
medal.sort(key= lambda x: -x[2])
medal.sort(key= lambda x: -x[1])

for i in range(1,n):
    if medal[i-1][1] == medal[i][1] and medal[i-1][2] == medal[i][2] and medal[i-1][3] == medal[i][3]:
        rank.append(rank[-1])
    else:
        rank.append(i+1)

for i in range(n):
    if medal[i][0] == k:
        print(rank[i])
        break
