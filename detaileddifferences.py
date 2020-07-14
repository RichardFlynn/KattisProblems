for _ in range(int(input())):
    w1=input()
    w2=input()
    print(w1)
    print(w2)
    out=""
    for i in range(len(w1)):
        if w1[i]==w2[i]:
            out+="."
        else:
            out+="*"
    print(out)
    print("")