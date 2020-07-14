rows,columns,newrows,newcolumns=map(int,input().split())
out=""
for r in range(rows):
    outrow=""
    row=input()
    for c in range(columns):
        outrow+=row[c]*newcolumns
    outrow+="\n"
    out+=outrow*newrows
print(out)