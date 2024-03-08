h = 6
for i in range(h):
    print("0"*(h-i)+"1"*(i*2+1)+"0"*(h-i))
print("1"*(h*2+1))

print("1"*(h*2+1))
for i in range(h,-1,-1):
    print("0"*(h-i)+"1"*(i*2+1)+"0"*(h-i))
