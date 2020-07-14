directions=input()


for n in range(1,6):
    if directions[:n]==directions[n:n+n]:
        print(len(directions)/n+len(directions)%n+n)