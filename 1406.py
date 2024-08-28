left = list(input())
right = []
n = int(input())
for i in range(n):
    cmd = input().split()
    if cmd[0] == "P":
        left.append(cmd[1])
    elif cmd[0] == "L" and left:
        right.append(left.pop())
    elif cmd[0] == "D" and right:
        left.append(right.pop())
    elif cmd[0] == "B" and left:
        left.pop()
    
print("".join(left)+"".join(right[::-1]))

