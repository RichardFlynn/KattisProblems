num,den=map(int,input().split())
while num!=0 or den!=0:
    print("{} {} / {}".format(num//den,num%den,den))
    num,den=map(int,input().split())