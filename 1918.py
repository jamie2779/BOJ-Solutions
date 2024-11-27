exp = input()
stack = []
order = {'+':1,'-':1,'*':2,'/':2}

for a in exp:
    if a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(a,end="")
    elif a == '(':
        stack.append(a)
    elif a == ')':
        while stack[-1] != '(':
            print(stack.pop(),end="")
        stack.pop()
    else:
        while stack and stack[-1] != '(' and order[stack[-1]]>=order[a]:
            print(stack.pop(),end="")
        stack.append(a)

while stack:
    print(stack.pop(),end="")
