from decimal import Decimal

expr = ['+', '-', '*', '/', '^', '(', ')', '#']

order = {'#':0,'^':2,'*':3,'/':3,'+':4,'-':4}

stack = []
back = []

ex = input()
i=0
digit = ''
while ex[i] != '=':
    if ex[i] in '0123456789':
        digit += ex[i]
        if ex[i+1] not in '0123456789':
            back.append(int(digit))
            digit = ''
    elif ex[i] == '(':
        stack.append(ex[i])
    elif ex[i] == ')':
        while True:
            now = stack.pop()
            if now == '(':
                break
            else:
                back.append(now)
    elif ex[i] == '#' or ex[i] == '^':
        while len(stack)>0 and stack[-1] != '(' and order[stack[-1]] < order[ex[i]]:
            back.append(stack.pop())
        stack.append(ex[i])
    else:
        while len(stack)>0 and stack[-1] != '(' and order[stack[-1]] <= order[ex[i]]:
            back.append(stack.pop())
        stack.append(ex[i])

    i+=1

while stack:
    back.append(stack.pop())
back.append('=')

#계산
stack = []
i=0
while back[i] != '=':
    if back[i] not in expr:
        stack.append(back[i])
    elif back[i] == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(b+a)
    elif back[i] == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif back[i] == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(b*a)
    elif back[i] == '/':
        a = stack.pop()
        b = stack.pop()
        a = Decimal(a)
        b = Decimal(b)
        stack.append(int(b/a))
    elif back[i] == '^':
        a = stack.pop()
        b = stack.pop()
        stack.append(b**a)
    elif back[i] == '#':
        a = stack.pop()
        a = Decimal(a)
        stack.append(int(a.sqrt()))
    i+=1

print(stack.pop())