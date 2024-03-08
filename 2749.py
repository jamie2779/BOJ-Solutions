#피사노 주기라는 수학적 지식을 이용하여 푸는 문제이다
#피보나치 수열의 나머지는 주기를 가지고 있고, 이를 피사노 주기라고 한다.
#주기의 길이가 p일 때, n번째 피보나치 수를 m으로 나눈 나머지는 n%p번째 피보나치 수를 m으로 나눈 나머지와 같다.
#주기의 길이는 m = 10^k (k>2)일때, 항상 15*10(k-1)이다

#이 문제에서는 k = 6이므로 주기는 15 * 10^5 = 1,500,000이다.

#처음코드 - 재귀 제한, 메모리초과
n = int(input())

def p(i,j,k,l):
    if k==l:
      print(i%1000000)
    else:
      p(j,i+j,k+1,l)
    
p(0,1,0,n)

#2차시도 - 시간초과
m = 1_000_000
p = 1_500_000
n = int(input())
n%=p

x,y = 0,1
for i in range(n-1):
    x,y = y,x+y
print(y%m)

#3차시도 - 시간초과 
m = 1_000_000
p = 1_500_000
n = int(input())
n%=p

x=0
y=1
tmp = 0
for i in range(n-1):
    tmp = x+y
    x = y
    y = tmp
print(y%m)

#4차시도-메모리 초과, 나누어서 저장으로 바꾸면 될듯
m = 1_000_000
p = 1_500_000
f = [0,1]

for i in range(2,p):
    f.append(f[i-1] + f[i-2])

n = int(input())
n%=p
print(f[n]%m)

#정답
m = 1_000_000
p = 1_500_000
f = [0,1]

for i in range(2,p):
    f.append(f[i-1] + f[i-2])
    f[i] %= m

n = int(input())
n%=p
print(f[n])