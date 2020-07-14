q=input()
p=2**(len(q)-1)
x=0
y=0
for n in q:
    if int(n)%2==1:
        x+=p
    if int(n)>1:
        y+=p
    p=p/2
print(len(q),int(x),int(y))