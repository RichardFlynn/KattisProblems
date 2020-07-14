parts,days=map(int,input().split())
part_list=[]
for x in range(days):
    newpart=input()
    part_list.append(newpart)
    if len(set(part_list))==parts:
        print(x+1)
        break
if len(set(part_list))!=parts:
    print("paradox avoided")