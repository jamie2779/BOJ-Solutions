from collections import defaultdict

def n36decode(n36):
    res = 0
    mul = 1
    for c in n36[::-1]:
        if ord(c)<58:
            res += int(c) * mul
        else:
            res += (ord(c)-55) * mul
        mul *= 36
    return res

def n36encode(n10):
    res = ""
    if n10 == 0:
        return 0
    while n10 >0:
        if n10%36 <10:
            res += str(n10%36)
        else:
            res += chr(n10%36 + 55)
        n10 //=36
    return res[::-1]

n = int(input())
nums = []
ch = []
alpha = defaultdict(lambda :0)
for i in range(n):
    nums.append(input())
    res = 0
    mul = 1
    for c in nums[-1][::-1]:
        if ord(c)<58:
            alpha[c] += (35-int(c)) * mul
        else:
            alpha[c] += (35-(ord(c)-55)) * mul
        mul *= 36


st = list(alpha.items())
st.sort(key=lambda x:x[1],reverse=True)
k = int(input())
k = min(k,len(st))
for i in range(k):
    ch.append(st[i][0])
s = 0
for num in nums:
    for i in range(k):
        num = num.replace(ch[i],'Z')
    s+= n36decode(num)
print(n36encode(s))
    
