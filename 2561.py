import itertools as it
import copy

def spin(l,rng):
    st = l[:rng[0]-1]
    rv = l[rng[0]-1:rng[1]]
    ed = l[rng[1]:]
    return st+rv[::-1]+ed

flag = False
n = int(input())
a = list(map(int,input().split()))


def makeTarget(l):
    target = [1]

    for i in range(n-1):
        diff = l[i] - l[i+1]
        if diff != 1 and diff != -1:
            target.append(i+1)
            target.append(i+2)
    if l[0] == 1:
        target = target[2:]

    if l[-1] == n:
        target = target[:-1]
    else:
        target.append(n)
        
    return target

def makeCase(target):
    case = set(it.combinations(set(target),2))
    case.add((1,1))
    return case

for i in makeCase(makeTarget(a)):
    c1 = copy.deepcopy(a)
    c1 = spin(c1,i)
    for j in makeCase(makeTarget(c1)):
        c2 = copy.deepcopy(c1)
        c2 = spin(c2,j)
        for k in makeCase(makeTarget(c2)):
            c3 = copy.deepcopy(c2)
            c3 = spin(c3,k)
            if c3 == list(range(1,n+1)):
                print(*i)
                print(*j)
                print(*k)
                flag = True
        if flag:
            break
    if flag:
        break