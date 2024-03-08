odds = []
for i in range(7):
    n = int(input())
    if n%2 == 1:
        odds.append(n)
if(len(odds)==0):
    print(-1)
else:
    print(sum(odds))
    print(min(odds))