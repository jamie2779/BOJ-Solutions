n = int(input())
nums = list(map(int,input().split()))
if n == 1:
    print(sum(nums) - max(nums))
else:
    min_1 = min(nums)
    case_2 =[]
    for i in range(6):
        for j in range(6):
            if i != j and i+j != 5:
                case_2.append(nums[i] + nums[j])
    min_2 = min(case_2)
    case_3 = []
    for i,j,k in ((0,4,3),(0,3,1),(0,4,2),(0,2,1),(5,4,3),(5,3,1),(5,4,2),(5,2,1)):
        case_3.append(nums[i] + nums[j] + nums[k])
    min_3 = min(case_3)

    cnt_3 = 4
    cnt_2 = 0
    cnt_1 = 0

    cnt_2 += (n-2)*4
    cnt_2 += (n-1)*4
    cnt_1 += (n-2)*(n-2)*5
    cnt_1 += (n-2)*4
    print(min_1 * cnt_1 + min_2*cnt_2 + min_3 * cnt_3)