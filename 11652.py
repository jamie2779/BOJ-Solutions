a = []
for _ in range(int(input())):
    name, s1,s2,s3 = input().split()
    a.append([name,int(s1),int(s2),int(s3)])

a.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))
for i in a:
    print(i[0])