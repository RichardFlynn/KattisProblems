from random import randint
allprobs=[10,10,10,10]
allprobs=sorted(allprobs,reverse=True)
for r in range(1,len(allprobs)+1):
    probs=allprobs[0:r]
    wins=[0,0,0,0,0]
    for _ in range(10000000):
        papers=0
        for i in range(len(probs)):
            if randint(1,100)<probs[i]:
                papers+=1
        wins[papers]+=1
    print(wins)
    E=0
    for i in range(1,r+1):
        #print((i**(i/r)),wins[i]/10000000)
        E+=(i**(i/r))*wins[i]/10000000
    print(E)
# wins=[0,0,0,0,0,0]
# probs=[60,60,60,60,60]
# for _ in range(1000000):
#     papers=0
#     for i in range(len(probs)):
#         if randint(1,100)<probs[i]:
#             papers+=1
#     wins[papers]+=1
# print(wins)