n=int(input())
while n!=0:
    tot=sum(map(int,str(n)))
    p=11
    while sum(map(int,str(p*n)))!=tot:
        p+=1
    print(p)
    n=int(input())