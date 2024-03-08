import sys
input = sys.stdin.readline
n = int(input())
r = sorted([int(input()) for _ in range(n)]) #n개 입력받고 정렬수행

if n == 0: #의견이 없으면 0 출력
    print(0)
else:
    cut = int((n*0.15)+0.5) #n의 15%를 반올림
    avg = sum(r[cut:n-cut]) / (n-2*cut) #평균 구하기
    print(int(avg + 0.5)) #평균을 반올림