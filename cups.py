colours=[]
for _ in range(int(input())):
    cup1,cup2=input().split()
    if ord(cup1[0])<58:
        colours.append([cup2,int(cup1)])
    else:
        colours.append([cup1,2*int(cup2)])
for i in sorted(colours,key=lambda x:x[1]):
    print(i[0])