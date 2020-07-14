def swap(a,b):
    temp=cups[a]
    cups[a]=cups[b]
    cups[b]=temp
cups=["0","",""]
swaps=input()
for l in swaps:
    if l=="A":
        swap(0,1)
    elif l=="B":
        swap(1,2)
    elif l=="C":
        swap(0,2)
    else:
        print("ERROR")
for c in range(len(cups)):
    if cups[c]=="0":
        print(c+1)
        break