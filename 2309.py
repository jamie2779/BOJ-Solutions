import itertools as it
n = map(input,['']*9)
n = map(int,n)
for p in it.permutations(n,7):
    if sum(p) == 100:
        print("\n".join(map(str,sorted(p))))

        break