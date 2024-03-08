n,m = map(int,input().split())
nl = {input() for _ in range(n)}
ns = {input() for _ in range(m)}
nls = sorted(nl & ns) #듣도못한 사람과 보도 못한 사람의 교집합
print(len(nls))
print('\n'.join(nls))