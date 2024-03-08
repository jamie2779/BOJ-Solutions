from collections import deque
n,m = map(int,input().split())
a = [*map(int,input().split())]
deck = deque(range(1,n+1))
cnt=0
for i in a:
    b = deck.index(i)
    if (len(deck)-1)//2 >= b:
        while deck[0] != i:
            cnt+=1
            deck.append(deck.popleft())
    else:
        while deck[0] != i:
            cnt+=1
            deck.appendleft(deck.pop())
    deck.popleft()
print(cnt)
