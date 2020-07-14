CIA=[]
for i in range(5):
    if "FBI" in input():
        CIA.append(i+1)
if CIA==[]:
    print("HE GOT AWAY!")
else:
    print(*CIA)