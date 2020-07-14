n=input()
while n!="0":
    orders={}
    for _ in range(int(n)):
        o=input().split()
        for i in range(1,len(o)):
            if o[i]not in orders:
                orders[o[i]]=[o[0]]
            else:
                orders[o[i]].append(o[0])
    for m in sorted(list(orders.items())):
        print(m[0],*m[1])
    orders.clear()
    n=input()