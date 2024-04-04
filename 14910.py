a = list(map(int,input().split()))
if a == sorted(a):
    print("Good")
else:
    print("Bad")