import sys
txt = []
for line in sys.stdin:
    txt += line.split()

count = 0
for t in txt:
    if t == "<br>":
        print()
        count = 0
    elif t == "<hr>":
        if count !=0:
            print()
        print("-"*80)
        count = 0
    else:
        if count+len(t)+1 > 80:  #한칸 띄우기 때문에 +1
            print()
            count = 0
        elif count > 0:    #줄의 첫부분에서는 공백을 출력하지 않아야 함
            print(end=" ")
            count += 1
        print(t,end="")
        count += len(t)
