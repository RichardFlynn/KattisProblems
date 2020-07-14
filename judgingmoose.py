t1,t2=map(int,input().split())
if t1+t2==0:
    print("Not a moose")
else:
    if t1==t2:
        p="Even"
    else:
        p="Odd"
    print(p,max(t1,t2)*2)
