#sys.stdin을 활용한 EOF 판단 구현
import sys
for line in sys.stdin:
	print(line)


#Try-Catch문을 활용한 EOF판단 구현 
while True:
	try:
		txt = input()
		print(txt)
	except EOFError:
	    break

	