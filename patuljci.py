def dwarfCheck():
    dwarves=[int(input())for _ in range(9)]
    target=sum(dwarves)-100
    for i in range(9):
        for j in range(i+1,9):
            if dwarves[i]+dwarves[j]==target:
                dwarves=dwarves[:i]+dwarves[i+1:j]+dwarves[j+1:]
                for d in dwarves:
                    print(d)
                return
dwarfCheck()
