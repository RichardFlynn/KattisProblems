from math import tan,cos,pi
g=9.81
def height(v,a,x):
    return x*tan(a*pi/180)-(g*(x**2))/(2*((v*cos(a*pi/180))**2))
for _ in range(int(input())):
    v,a,x,lh,uh=map(float,input().split())
    h=height(v,a,x)
    if h-lh<1 or uh-h<1:
        print("Not Safe")
    else:
        print("Safe")