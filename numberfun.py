for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a+b==c or a*b==c or abs(a-b)==c or max(a,b)/min(a,b)==c:
        print("Possible")
    else:
        print("Impossible")
        