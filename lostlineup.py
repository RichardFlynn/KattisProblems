n=int(input())-1
order=list(map(int,input().split()))
line=[1]
line.extend([0 for x in range(n)])
for i in range(n):
    line[order[i]+1]=i+2
print(*line)