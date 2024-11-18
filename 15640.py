en = []
st = []

i = 1
while True:
    if i>100:
        break
    en.append(i)
    i+=1
    if i>100:
        break
    en.append(i)
    i+=1
    if i>100:
        break
    st.append(i)
    i+=1

print(100, 2,len(st))
for i in range(len(st)):
    print(st[i],en[i])