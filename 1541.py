a = input().split('-')
answer = sum(map(int,a[0].split('+')))
for i in a[1:]:
    answer -= sum(map(int,i.split('+')))
print(answer)