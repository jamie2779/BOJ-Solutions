import sys

a = input()
print(len(a))  #

b = sys.stdin.readline()
print(len(b))


import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline().split()

import sys
input = sys.stdin.readline #한번 써두면 이후의 input은 모두 sys.stdin.readline으로 작동함
a = input()
print(a)