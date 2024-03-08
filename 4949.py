while True:
    text = input()
    b = []
    if text == '.':
        break
    for c in text:
        if c == '(' or c == '[':
            b.append(c)
        elif c == ')':
            if b and b[-1] == '(':
                b.pop()
            else:
                b = ['no']
                break
        elif c == ']':
            if b and b[-1] == '[':
                b.pop()
            else:
                b = ['no']
                break
    if len(b) == 0:
        print('yes')
    else:
        print('no')

