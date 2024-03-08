n = int(input())
answer = list(input())
for i in range(n-1):
    target = input()
    for j in range(len(answer)):
        if answer[j] != '?' and target[j] != answer[j]:
            answer[j] = '?'
print(''.join(answer))