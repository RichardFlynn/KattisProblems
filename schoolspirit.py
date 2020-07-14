scores=[]
for _ in range(int(input())):
    scores+=[int(input())]
print(sum([scores[i]*(4/5)**i for i in range(len(scores))])/5)
print(sum([sum([[scores[:j]+scores[j+1:]][0][i]*(4/5)**i for i in range(len(scores)-1)])/5 for j in range(len(scores))])/len(scores))