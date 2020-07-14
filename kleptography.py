k,m=map(int,input().split())
txt=input()
cip=input()
for i in range(1,m-k+1):
    txt=chr((ord(cip[-i])-97-ord(txt[-i])+97)%26+97)+txt
print(txt)