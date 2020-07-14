c,p=input().split()
mid="ex"
if c[-2:]=="ex":
    mid=""
elif c[-1]=="e":
    mid="x"
elif c[-1]in"aiou":
    c=c[:-1]
print(c+mid+p)