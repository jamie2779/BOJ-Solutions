cnt=0
for i in range(int(input())):
    st = []
    for j in range(input()):
        if st and st[-1]==j:
            st.pop()
        else:
            st.append(j)
    if len(st)==0:
        cnt+=1
print(cnt)