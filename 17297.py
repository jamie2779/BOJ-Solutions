n = int(input())
ls = [5,13]
while ls[-1] < n:
    ls.append(ls[-1]+ls[-2]+1)
def f(k,c):
    if k<2:
        if c == 6:
            return "Messi Messi Gimossi"
        else:
            return 'Messi Gimossi'[c-1]

    
    if ls[k-1]+1 == c:
        return "Messi Messi Gimossi"
    elif ls[k-1] >= c:
        return f(k-1,c)
    else:
        return f(k-2,c-1-ls[k-1])
print(f(len(ls)-1,n))
# ls = []
# def f(k,c):
#     if k<2:
#         return 'Messi Gimossi'[c-1]
    
#     if ls[k-1]+1 == c:
#         return " "
#     elif ls[k-1] >= c:
#         return f(k-1,c)
#     else:
#         return f(k-2,c-1-ls[k-1])
        
# def a(n):
#     global ls
#     ls = [5,13]
#     while ls[-1] < n:
#         ls.append(ls[-1]+ls[-2]+1)
#     return f(len(ls)-1,n)

# st = ['Messi','Messi Gimossi']
# c = 0
# while True:
#     c+=1
#     if len(st[-1]) >= c:
#         if st[-1][c-1] != a(c):
#             print(c)
#             print(f"{st[-1][c-1]} != {a(c)}")
#             break
#     else:
#         st.append(st[-1]+' ' + st[-2])
#     if c%1000000 == 0:
#         print(f"{c} ({c/1073741823*100:.3f}%)")

