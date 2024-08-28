x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())

def det(p1,p2):
    return p1[0]*p2[1] - p1[1]*p2[0]

def vec(p1,p2):
    return (p2[0]-p1[0],p2[1]-p1[1])
def isCross(p0,p1,p2,p3):
    d0 = det(vec(p0,p2),vec(p0,p3))
    d1 = det(vec(p1,p2),vec(p1,p3))
    d2 = det(vec(p2,p0),vec(p2,p1))
    d3 = det(vec(p3,p0),vec(p3,p1))

    print(d0,d1,d2,d3)
    if d0*d1 < 0 and d2*d3<0:
        return 1
    else:
        return 0


print(isCross((x1,y1),(x2,y2),(x3,y3),(x4,y4)))