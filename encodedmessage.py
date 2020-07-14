for _ in range(int(input())):
    o=""
    p=input()
    for i in range(1,int(len(p)**0.5)+1):
        for j in range(1,int(len(p)**0.5)+1):
            o+=p[int(len(p)**0.5)*j-i]
    print(o)