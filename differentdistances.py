a=input()
while a!="0":
    x1,y1,x2,y2,p=map(float,a.split())
    print("{:.10f}".format((abs(x1-x2)**p+abs(y1-y2)**p)**(1/p)))
    a=input()