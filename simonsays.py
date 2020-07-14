def simon(s):
    if s[0:10]=="Simon says":
        return True
    return False
orders=[]
for _ in range(int(input())):
    orders.append(input())
for o in filter(simon,orders):
    print(o[11:])