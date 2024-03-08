n,k = map(int,input().split())
name = list(map(int,input().split()))
tap = [0] * n
i=0
answer = 0
while i<k:
    if name[i] in tap:
        i+=1
        continue

    for j in range(n):
        if tap[j] == 0:
            tap[j] = name[i]
            i+=1
            break
    else:
        nextPos = [k] * n
        for j in range(n):
            for l in range(i,k):
                if name[l] == tap[j]:
                    nextPos[j] = l
                    break
        
        maxPos = 0
        maxVal = nextPos[0]

        for j in range(n):
            if maxVal < nextPos[j]:
                maxPos = j
                maxVal = nextPos[j]
        
        tap[maxPos] = 0 
        answer += 1
print(answer)