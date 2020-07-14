n=int(input())
count=1
while n!=0:
    print("SET {}".format(count))
    listend=[]
    for _ in range(n//2):
        print(input())
        listend+=[input()]
    if n%2==1:
        print(input())
    for i in range(n//2):
        print(listend[n//2-1-i])
    count+=1
    n=int(input())