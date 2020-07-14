def eucDis(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

px,py,x1,y1,x2,y2=map(int,input().split())
closest=[0,0]
if px<=x1:
    closest[0]=x1
elif px>=x2:
    closest[0]=x2
else:
    closest[0]=px
if py<=y1:
    closest[1]=y1
elif py>=y2:
    closest[1]=y2
else:
    closest[1]=py
print("{:.3}".format(eucDis((px,py),closest)))