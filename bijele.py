numbers=list(map(int,input().split()))
require=[1,1,2,2,2,8]
out=""
for i in range(6):
    out+=str(require[i]-numbers[i])
    out+=" "
print(out)