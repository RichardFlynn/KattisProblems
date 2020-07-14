from math import floor
prec,dis=map(int,input().split())
votes={x+1:[0,0] for x in range(dis)}
for p in range(prec):
    d,a,b=map(int,input().split())
    votes[d]=[votes[d][0]+a,votes[d][1]+b]
totWa=0
totWb=0
for v in votes.values():
    if v[0]>v[1]:
        winner="A"
        Wa=v[0]-floor((v[0]+v[1])/2)-1
        Wb=v[1]
    else:
        winner="B"
        Wa=v[0]
        Wb=v[1]-floor((v[1]+v[0])/2)-1
    totWa+=Wa
    totWb+=Wb
    print(winner,Wa,Wb)
print("{:.10f}".format(abs(totWa-totWb)/sum(map(sum,votes.values()))))
    