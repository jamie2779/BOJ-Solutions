from math import isqrt
def div(a,b):
    if a>=0:
        if b>=0:
            return a//b
        else:
            return -(a//-b)
    else:
        if b>=0:
            return -(-a//b)
        else:
            return (-a//-b)

a = input()
while a.find("#") != -1:
    i = a.find("#")
    j = i+1
    if a[j] == "(" or a[j] == "i" or a[j] == "s":
        st=1
        j+=1
        while st>0:
            if a[j] == "(":
                st += 1
            elif a[j] == ")":
                st -= 1
            j+=1
    while j < len(a) and a[j] in ('1','2','3','4','5','6','7','8','9','0','#'):
        j+=1
    if j>=len(a):
        a = a+ ")"
    else:
        a = a[:j] + ")" + a[j:]
    a = a[:i] +"s"+ a[i+1:]

while a.find("/") != -1:
    i = a.find("/")
    a = a[:i] +"d"+ a[i+1:]

    j = i+1
    if a[j] == "(" or a[j] == "i" or a[j] == "s":
        st=1
        j+=1
        while st>0:
            if a[j] == "(":
                st += 1
            elif a[j] == ")":
                st -= 1
            j+=1
    while j < len(a) and a[j] in ('1','2','3','4','5','6','7','8','9','0','#'):
        j+=1
    if j>=len(a):
        a = a+ ")"
    else:
        a = a[:j] + ")" + a[j:]
    
    j = i-1
    if a[j] == ")":
        st=-1
        j-=1
        while st<0:
            if a[j] == "(" or a[j] == "i" or a[j] == "s":
                st += 1
            elif a[j] == ")":
                st -= 1
            j-=1
    while j >=0 and a[j] in ('1','2','3','4','5','6','7','8','9','0','#'):
        j-=1
    if j<0:
        a = "i" + a
    else:
        a = a[:j+1] + "i" + a[j+1:]

a = a.replace("^","**")
a = a.replace("d",",")
a = a.replace("i","div(")
a = a.replace("s","isqrt(")

print(int(eval(a[:-1])))