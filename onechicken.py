p,c=map(int,input().split())
s="s"
if abs(c-p)==1:
    s=""
if p<c:
    print("Dr. Chaz will have {} piece{} of chicken left over!".format(c-p,s))
else:
    print("Dr. Chaz needs {} more piece{} of chicken!".format(p-c,s))