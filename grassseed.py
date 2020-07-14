from functools import reduce
size=float(input())
total=0
for _ in range(int(input())):
    total+=size*reduce(lambda x,y:x*y,(map(float,input().split())))
print(total)