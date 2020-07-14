def baseConvert(n,b):
    total=[]
    while n>0:
        total+=[n%b]
        n=n//b
    return total

def sumSquare(digits):
    return sum(map(lambda x:int(x)**2,digits))

for _ in range(int(input())):
    case,base,num=map(int,input().split())
    print(case,sumSquare(baseConvert(num,base)))