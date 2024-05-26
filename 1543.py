a = input()
b = input()

st = 0
ans = 0
while st < len(a):
    st = a.find(b,st)
    if st == -1:
        break
    ans += 1
    st += len(b)
print(ans)