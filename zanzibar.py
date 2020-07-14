for _ in range(int(input())):
    imports=0
    turts=list(map(int,input().split()))[:-1]
    for i in range(1,len(turts)):
        imports+=max(0,turts[i]-2*turts[i-1])
    print(imports)