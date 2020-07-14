from collections import Counter
n=int(input())
board=[]
par=True
for _ in range(n):
    board.append([c for c in input()])
for i in range(n):
    if Counter(board[i])["B"]!=n/2 or Counter(list(zip(*board))[i])["B"]!=n/2:
        par=False
for s in board:
    for c in range(n-2):
        if s[c]+s[c+1]+s[c+2]=="WWW" or s[c]+s[c+1]+s[c+2]=="BBB":
            par=False
for s in list(zip(*board)):
    for c in range(n-2):
        if s[c]+s[c+1]+s[c+2]=="WWW" or s[c]+s[c+1]+s[c+2]=="BBB":
            par=False
if par:
    print(1)
else:
    print(0)