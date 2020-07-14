def checkLuhn(n):
    total=0
    for i in range(len(n)):
        d=int(n[len(n)-1-i])
        if i%2==1:
            d=2*d
            if d>9:
                d-=9
        total+=d
    if total%10==0:
        return "PASS"
    return "FAIL"

for _ in range(int(input())):
    print(checkLuhn(input()))