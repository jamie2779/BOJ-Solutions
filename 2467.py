n = int(input())
liq = list(map(int,input().split()))
liq.sort()

min_a = liq[0]
min_b = liq[-1]
min_val = abs(min_a + min_b)

def binsearch(start, end, value):
    global min_a
    global min_b
    global min_val
    mid = 0
    while start<=end:
        mid = (start+end)>>1
        mix = liq[mid] + value
        
        if abs(mix) < min_val:
            min_a = value
            min_b = liq[mid]
            min_val = abs(mix)

        if mix==0:
            break
        elif mix>0:
            end = mid-1
        else:
            start = mid+1
    return liq[mid]




for i in range(n-1):    
    if min_val == 0:
        break

    b = binsearch(i+1,n-1,liq[i])


print(min_a,min_b)