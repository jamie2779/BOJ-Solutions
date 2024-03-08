from collections import deque
n = int(input())
cards = deque(range(1,n+1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards[0])
    cards.popleft()

print(cards[0])