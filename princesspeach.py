obstacles,found=map(int,input().split())
mario=[]
for i in range(found):
    mario.append(int(input()))
for i in range(obstacles):
    if i not in mario:
        print(i)
print("Mario got {} of the dangerous obstacles.".format(len(set(mario))))