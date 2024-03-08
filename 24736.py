#map에 인자 여러개 가능
a = map(int,input().split())
b = map(int,input().split())
s = [6,3,2,1,2]
print(sum(map(lambda x,y:x*y,a,s )))
print(sum(map(lambda x,y:x*y,b,s )))