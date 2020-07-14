total=0
for _ in range(int(input())):
    a,b=map(float,input().split())
    total+=a*b
print("{:.3f}".format(total))