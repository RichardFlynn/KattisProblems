l,x=map(int,input().split())
t=0
r=0
for i in range(x):
    o,p=input().split()
    if o=="enter":
        if int(p)+t<=l:
            t+=int(p)
        else:
            r+=1
    else:
        t-=int(p)
print(r)