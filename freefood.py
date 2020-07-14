from functools import reduce
events=[]
for _ in range(int(input())):
    start,end=map(int,input().split())
    events.append(set(range(start,end+1)))
print(len(reduce(lambda x,y:x.union(y),events)))