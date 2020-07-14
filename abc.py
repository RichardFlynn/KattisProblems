n1,n2,n3=map(int,input().split())
order=input()
abc={'A':min(n1,n2,n3),'B':max(min(n1,n2),min(n2,n3),min(n1,n3)),'C':max(n1,n2,n3)}
print(abc[order[0]],abc[order[1]],abc[order[2]])