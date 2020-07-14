n=int(input())
while n!=-1:
    matr=[list(map(int,input().split()))for _ in range(n)]
    unsupported=[]
    for r in range(n):
        support=False
        edges=[]
        for c in range(n):
            if matr[r][c]==1:
                edges+=[c]
        for i in range(len(edges)):
            for j in range(i+1,len(edges)):
                if matr[edges[i]][edges[j]]:
                    support=True
        if not support:
            unsupported+=[r]
    print(*unsupported)    
    n=int(input())