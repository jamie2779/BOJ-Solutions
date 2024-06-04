a = int(input())
if a in [1,3]:
    print(-1)
else:
    five = a//5
    if a%5 in [1,3]:
        five -= 1
    a -= 5*five
    print(five + a//2)