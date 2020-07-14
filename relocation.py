c,q=map(int,input().split())
lc=list(map(int,input().split()))
for _ in range(q):
    o=list(map(int,input().split()))
    if o[0]==1:
        lc[o[1]-1]=o[2]
    elif o[0]==2:
        print(abs(lc[o[1]-1]-lc[o[2]-1]))