text=input()
wordlen=int(len(text)/3)
t1=text[:wordlen]
t2=text[wordlen:2*wordlen]
t3=text[2*wordlen:]
if t1==t2:
    print(t1)
else:
    print(t3)