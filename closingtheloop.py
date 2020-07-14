for t in range(int(input())):
    input()
    rope=[]
    rs=[]
    bs=[]
    for s in input().split():
        if s[-1]=="R":
            rs.append(int(s[:-1]))
        else:
            bs.append(int(s[:-1]))
    rs=sorted(rs)
    bs=sorted(bs)
    for i in range(min(len(rs),len(bs))):
        rope.append(rs.pop())
        rope.append(bs.pop())
    print("Case #"+str(t+1)+":",sum(rope)-len(rope))