
expr = ['+', '-', '*', '/','(', ')']

order = {'*':1,'/':1,'+':2,'-':2}

stack = []
back = []

ex = input()
try:
    i=0
    digit = ''
    while i<len(ex):
        if ex[i] in '0123456789':
            digit += ex[i]
            if i+1 >=len(ex) or ex[i+1] not in '0123456789':
                if i+1<len(ex) and ex[i+1] == '(':
                    raise
                back.append(int(digit))
                digit = ''
        elif ex[i] == '(':
            if i+1<len(ex) and ex[i+1] == ')':
                raise
            stack.append(ex[i])
        elif ex[i] == ')':
            if i+1<len(ex) and ex[i+1] in "0123456789":
                raise
            while True:
                now = stack.pop()
                if now == '(':
                    break
                else:
                    back.append(now)
        else:
            while len(stack)>0 and stack[-1] != '(' and order[stack[-1]] <= order[ex[i]]:
                back.append(stack.pop())
            stack.append(ex[i])

        i+=1

    while stack:
        back.append(stack.pop())
        if back[-1] == '(':
            raise

    #계산
    stack = []
    i=0
    while i<len(back):
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
            stack.append(b//a)
        i+=1

    print(stack.pop())
except:
    print("ROCK")