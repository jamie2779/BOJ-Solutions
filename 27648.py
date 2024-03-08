n, m, k = map(int,input().split())
if k>= m+n -1:
    print("YES")	
    for i in range(n):
        for j in range(m):
            print(i+j+1,end=" ")
        print()
else:
    print("NO")