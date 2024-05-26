import sys
sys.setrecursionlimit(10**8)
std = sys.stdin.readlines()
root = int(std[0].strip())
right = {}
left = {}
def addNode(n):
    now = root 
    while True:
        if n < now:
            if now in left:
                now = left[now]
            else:
                left[now] = n
                break
        else:
            if now in right:
                now = right[now]
            else:
                right[now] = n
                break

def postOrderPrint(n):
    if n in left:
        postOrderPrint(left[n])
    if n in right:
        postOrderPrint(right[n])
    print(n)
    
for i in std[1:]:
    addNode(int(i))

postOrderPrint(root)
