from collections import Counter
spaces={0:0,1:0,2:0,3:0,4:0}
row,column=map(int,input().split())
city=[]
for r in range(row):
    newrow=[]
    for c in input():
        newrow.append(c)
    city.append(newrow)
for ir in range(row-1):
    for ic in range(column-1):
        sqr=(city[ir][ic],city[ir+1][ic],city[ir][ic+1],city[ir+1][ic+1])
        if "#" not in sqr:
            spaces[Counter(sqr)['X']]+=1
for s in spaces.values():
    print(s)