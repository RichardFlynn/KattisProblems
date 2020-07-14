p=[]
max=0
for i in range(5):
    p.append(sum(map(int,input().split())))
    if p[i]>p[max]:
        max=i
print(max+1,p[max])