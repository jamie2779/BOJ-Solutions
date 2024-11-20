t =input()

cap = False

res = 0

for i in range(len(t)):
    res += 1
    if t[i].isupper() != cap:
        res += 1
        if i+1<len(t) and t[i+1].isupper() != cap:
            cap = t[i].isupper()
print(res)