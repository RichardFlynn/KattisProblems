g=sum(map(int,input().split()))
e=sum(map(int,input().split()))
if e>g:
    print("Emma")
elif g>e:
    print("Gunnar")
else:
    print("Tie")