i = list(map(int,input().split()))
a,b = min(i), max(i)
print(max(b-a-1,0))

print(" ".join(map(str,range(a+1,b))))
#for i in range(a+1,b):
#    print(i,end=' ')
