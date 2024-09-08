import heapq

n = int(input())
row = list(map(int, input().split()))
cp = list(map(int, input().split()))

a = [[0] * n for _ in range(n)]

def valid():
    for j in range(n):
        judge = sum(a[i][j] for i in range(n))
        if judge != cp[j]:
            return False
    return True

col = []
for i in range(n):
    heapq.heappush(col, (-cp[i], i))  

for i in range(n):
    temp = []
    
    for j in range(row[i]):
        pv = heapq.heappop(col)
        a[i][pv[1]] = 1
        temp.append((pv[0] + 1, pv[1]))  
    
    for item in temp:
        heapq.heappush(col, item)

if not valid():
    print("-1")
else:
    print("1")
    for row in a:
        print("".join(map(str, row)))