input()
unis=[]
while len(unis)<12:
    uni,team=input().split()
    if uni not in unis:
        unis.append(uni)
        print(uni,team)