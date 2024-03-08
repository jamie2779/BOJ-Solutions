n,m = map(int,input().split())
package = []
single = []
for i in range(m):
    p,s = map(int,input().split())
    package.append(p)
    single.append(s)

min_package = min(package)
min_single = min(single)

total = min((n//6+1)*min_package, n//6*min_package + n%6*min_single, n * min_single)

print(total)