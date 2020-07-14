for _ in range(int(input())):
    num,pq=input().split()
    p,q=map(int,pq.split("/"))
    path=[]
    while p!=1 or q!=1:
        if p<q:
            p=p
            q=q-p
            path.append(-1)
        elif p>q:
            p=p-q
            q=q
            path.append(1)
    d=len(path)
    al=0
    for s in range(1,d+1):
        if path[d-s]>0:
            al+=(2**d)/(2**s)
        
    print(num,int(2**d-1+al+1))