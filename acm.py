from collections import Counter
x=input()
log=[]
while x!='-1':
    log.append(x.split())
    x=input()
correct=[]
time=0
for rec in log:
    if rec[2]=='right':
        time+=int(rec[0])
        correct.append(rec[1])
for prob in correct:
    time+=20*(Counter(list(zip(*log))[1])[prob]-1)
print(len(correct),time)
