scores={"A":(11,11),"K":(4,4),"Q":(3,3),"J":(20,2),"T":(10,10),"9":(14,0),"8":(0,0),"7":(0,0)}
rounds,suit=input().split()
total=0
for _ in range(4*int(rounds)):
    card=input()
    dom=1
    if card[1]==suit:
        dom=0
    total+=scores[card[0]][dom]
print(total)