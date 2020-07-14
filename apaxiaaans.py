name=input()
out=""
for c in range(len(name)-1):
    if name[c]!=name[c+1]:
      out+=name[c]
print(out+name[len(name)-1])