from collections import Counter
for case in range(int(input())):
    input()
    invites=input().split()
    for i in Counter(invites):
        if Counter(invites)[i]==1:
            print("Case #{}: {}".format(case+1,i))
            break