# mn, mx = map(int,input().split())

# cnt = mx-mn+1
# ignore = [False] * (int(mx**0.5)-1)
# sqnumbers = []
# for i in range(2, int(mx**0.5)+1):
#     if i not in ignore:
#         sqnumbers.append(i*i)
#         ignore += list(range(i,int(mx**0.5)+1,i))


# for i in range(mn, mx+1):
#     for j in sqnumbers:
#         if i % j == 0:
#             cnt -= 1
#             break
# print(cnt)

mn, mx = map(int,input().split())

cnt = mx-mn+1
memo = [True] * (mx-mn + 1)

for i in range(2,int(mx**0.5)+1):
    for j in range((mn//(i*i))*(i*i),mx+1,i*i):
        if j-mn >= 0 and memo[j-mn]:
            cnt -= 1
            memo[j-mn] = False
print(cnt)