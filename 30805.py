_,a,_,b = [input() for _ in range(4)]
a = a.split()
b = b.split()
mx = ""

def cell(i,j,now):
    global mx
    mx = max(now,mx)
    if i>=len(a) or j>=len(b):
        return
    for k in range(j,len(b)):
        if a[i] == b[k]:
            cell(i+1, j+1, now + a[i])
    cell(i+1,j,now)

cell(0,0,"")

print(len(mx))
print(" ".join(mx))