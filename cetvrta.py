from collections import Counter
x=[0,0,0]
y=[0,0,0]
for i in range(3):
    x[i],y[i]=input().split()
print([a for a in x if Counter(x)[a]==1][0],[b for b in y if Counter(y)[b]==1][0])