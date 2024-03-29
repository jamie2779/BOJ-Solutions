from collections import deque
a = deque(input())
target = deque(input())
test = deque()
stack = deque()
n = len(target)

while len(a) >0:
    test.append(a.popleft())
    if len(test) >n:
        stack.append(test.popleft())
    if len(test) == n:
        if test == target:
            test.clear()
            for i in range(min(n,len(stack))):
                a.appendleft(stack.pop())

stack += test
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))

    
    