m,n=map(int,input().split())
words={}
for _ in range(m):
    word,score=input().split()
    words[word]=int(score)
for _ in range(n):
    total=0
    line=input()
    while line!=".":
        for w in line.split():
            if w in words:
                total+=words[w]
        line=input()
    print(total)