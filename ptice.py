N=int(input())
t=input()
Adrian=['A','B','C']
Bruno=['B','A','B','C']
Goran=['C','C','A','A','B','B']
acount=0
bcount=0
gcount=0
for i in range(N):
    if t[i]==Adrian[i%3]:
        acount+=1
    if t[i]==Bruno[i%4]:
        bcount+=1
    if t[i]==Goran[i%6]:
        gcount+=1
big=max(max(acount,bcount),gcount)
print(big)
if acount==big:
    print("Adrian")
if bcount==big:
    print("Bruno")
if gcount==big:
    print("Goran")