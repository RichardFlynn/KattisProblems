input()
junklist=list(map(int,input().split()))
smallest=0
for i in range(1,len(junklist)):
    if junklist[i]<junklist[smallest]:
        smallest=i
print(smallest)