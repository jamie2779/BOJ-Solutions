d = []
for i in range(10):
    d.append(input())

#1이 있는 영역의 양 꼭짓점 확인
min_x,min_y = 9,9
max_x,max_y = 0,0
for i in range(10):
    for j in range(10):
        if d[i][j] == "1":
            if i < min_y:
                min_y = i
            elif i > max_y:
                max_y = i
            if j < min_x:
                min_x = j
            elif j > max_x:
                max_x = j

#직각 이등변 삼각형이 가능한 가로, 세로 인지 확인
w = max_x - min_x
h = max_y - min_y
#1이 있는 부분만 잘라내기
frame = []
comp = []
for i in range(min_y,max_y+1):
    frame.append(d[i][min_x:max_x+1])

#방향별 삼각형 비교
if h/2 == w:
    if frame[0][0] == '1':
        for i in range(h//2):
            comp.append("1"*(i+1)+"0"*(w-i))
        comp.append("1"*(w+1))
        for i in range(h//2-1,-1,-1):
            comp.append("1"*(i+1)+"0"*(w-i))

        if frame == comp :    
            print(min_y+1, min_x+1) #왼쪽 위                    #10
            print((min_y + max_y)//2+1, max_x+1) #오른쪽 중간    #11
            print(max_y+1, min_x+1) #왼쪽 아래                  #10
        else:
            print(0)              
    else:
        for i in range(h//2):
            comp.append("0"*(w-i)+"1"*(i+1))
        comp.append("1"*(w+1))
        for i in range(h//2-1,-1,-1):
            comp.append("0"*(w-i)+"1"*(i+1))

        if frame == comp :    
            print(min_y+1, max_x+1) #오른쪽 위                  #01
            print((min_y + max_y)//2+1, min_x+1) #왼쪽 중간      #11
            print(max_y+1, max_x+1) #오른쪽 아래                #01
        else:
            print(0)
elif w/2 == h:
    if frame[0][0] == '1':
        for i in range(h,-1,-1):
            comp.append("0"*(h-i)+"1"*(i*2+1)+"0"*(h-i))
        if frame == comp :  
            print(min_y+1, min_x+1) #왼쪽 위                   #111
            print(min_y+1, max_x+1) #오른쪽 위                 #010
            print(max_y+1, (min_x+max_x)//2+1) #가운데 아래
        else:
            print(0)
    else:
        for i in range(h+1):
            comp.append("0"*(h-i)+"1"*(i*2+1)+"0"*(h-i))
        if frame == comp :  
            print(min_y+1, (min_x+max_x)//2+1) #가운데 위       #010
            print(max_y+1, min_x+1) #왼쪽 아래                  #111
            print(max_y+1, max_x+1) #오른쪽 아래
        else:
            print(0)
elif h == w and frame != []:
    if frame[0][0] == '0':
        for i in range(h+1):
            comp.append("0"*(h-i)+"1"*(i+1))
        if frame == comp :
            print(min_y+1, max_x+1) #오른쪽 위                 #001
            print(max_y+1, min_x+1) #왼쪽 아래                 #011
            print(max_y+1, max_x+1) #오른쪽 아래               #111
        else:
            print(0)
    elif frame[0][-1] =='0':
        for i in range(h+1):
            comp.append("1"*(i+1)+"0"*(h-i))
        if frame == comp :
            print(min_y+1, min_x+1) #왼쪽 위                   #100
            print(max_y+1, min_x+1) #왼쪽 아래                 #110
            print(max_y+1, max_x+1) #오른쪽 아래               #111
        else:
            print(0)
    elif frame[-1][0] == '0':
        for i in range(h,-1,-1):
            comp.append("0"*(h-i)+"1"*(i+1))
        if frame == comp :
            print(min_y+1, min_x+1) #왼쪽 위                   #111
            print(min_y+1, max_x+1) #오른쪽 위                 #011
            print(max_y+1, max_x+1) #오른쪽 아래               #001
        else:
            print(0)
    else:
        for i in range(h,-1,-1):
            comp.append("1"*(i+1)+"0"*(h-i))
        if frame == comp :
            print(min_y+1, min_x+1) #왼쪽 위                   #111
            print(min_y+1, max_x+1) #오른쪽 위                 #110
            print(max_y+1, min_x+1) #왼쪽 아래                 #100
        else:
            print(0)
else:
    print(0)