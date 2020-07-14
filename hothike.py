n=int(input())
temps=list(map(int,input().split()))
days=sorted([(x,x+2) for x in range(0,n-2)],key=lambda x:max(map(lambda y:temps[y],x)))[0]
print(days[0]+1,max(map(lambda y:temps[y],days)))