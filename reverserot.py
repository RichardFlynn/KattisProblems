def rev(s):
    r=""
    for c in s:
        r=c+r
    return r
def toNum(s):
    n=[]
    for c in s:
        if c=="_":
            n.append(26)
        elif c==".":
            n.append(27)
        else:
            n.append(ord(c)-65)
    return n
def rot(s,k):
    for i in range(len(s)):
        s[i]=(s[i]+k)%28
    return s
def toChar(s):
    c=""
    for n in s:
        if n==26:
            c+="_"
        elif n==27:
            c+="."
        else:
            c+=chr(n+65)
    return c
a=input()
tt=[]
while a!="0":
    tt.append(a.split())
    a=input()
for x in tt:
    x[1]=toChar(rot(toNum(rev(x[1])),int(x[0])))
    print(x[1])