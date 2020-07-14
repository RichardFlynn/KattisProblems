
valids={('*****', '*   *', '*****'):0,('     ', '     ', '*****'):1,('* ***', '* * *', '*** *'):2,('* * *', '* * *', '*****'):3,('***  ', '  *  ', '*****'):4,('*** *', '* * *', '* ***'):5,('*****', '* * *', '* ***'):6,('*    ', '*    ', '*****'):7,('*****', '* * *', '*****'):8,('*** *', '* * *', '*****'):9}

check=True
nums=zip(*[input() for _ in range(5)])
n=""
for t in nums:
    for c in t:
        n+=c
    n+="_"
nums=map(lambda x:tuple((x+"*").split("_"))[:3],n.split("*_     _"))
realnum=""
for n in nums:
    if n not in valids:
        check=False
    else:
        realnum+=str(valids[n])
#print(realnum)
if check and int(realnum)%6==0:
    print("BEER!!")
else:
    print("BOOM!!")