x=bin(int(input()))[2:]
out=""
for i in x:
    out=i+out
print(int(out,2))